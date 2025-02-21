from fastapi import FastAPI, HTTPException
from models import SearchRequest, SearchResponse
from fastapi.middleware.cors import CORSMiddleware
from app.retriever import load_rag_model
from app.generator import load_generator_model
import torch
import time
from PIL import Image
from transformers.image_utils import load_image
from utils import encode_image
from contextlib import asynccontextmanager
    
rag_models = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    print(f"loading rag model.")
    rag_models["RAG"] = load_rag_model()
    print(f"successfully loaded model.")
    
    print(f" loading the smollVLM model.")
    rag_models["gen_model"], rag_models["processor"]  = load_generator_model()
    print(f" successfully loadded smollVLMM model")
    yield
    # Clean up the ML models and release the resources
    rag_models.clear()

app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:5173",  # Your React frontend URL
    "http://127.0.0.1:5173",  # Alternative URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow frontend requests
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (POST, GET, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.post("/search", response_model=SearchResponse)
async def rag_search(query: SearchRequest) -> SearchResponse:
    s = time.perf_counter()
    results = rag_models["RAG"].search(query.query, k=2)
    
    for i, result in enumerate(results):
        print(f"result ({1}) doc: {result.doc_id} page: {result.page_num}")
    
    print(f" get result from the rag {time.perf_counter() - s} seconds")
    images = [load_image(result.base64) for result in results]
    encoded_images = [result.base64 for result in results]
    
    messages =  construct_message(query.query)
    prompt = rag_models["processor"].apply_chat_template(messages, add_generation_prompt=True)
    inputs = rag_models["processor"](text=prompt, images=images, return_tensors="pt")
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    inputs = inputs.to(DEVICE)

    # Generate outputs
    generated_ids = rag_models["gen_model"].generate(**inputs, max_new_tokens=500)
    generated_texts = rag_models["processor"].batch_decode(
        generated_ids,
        skip_special_tokens=True,
    )

    print(generated_texts[0])    
    print(f" generated response in {time.perf_counter() - s} seconds")
    return SearchResponse(results= generated_texts[0], images=encoded_images)
    
    

def construct_message(query):
    # Create input messages
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image"},
                {"type": "image"},
                {"type": "text", "text": query}
            ]
        },
    ]
    return messages