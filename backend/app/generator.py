from transformers import AutoProcessor, AutoModelForVision2Seq, BitsAndBytesConfig
import torch
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


def load_generator_model():
    quantization_config = BitsAndBytesConfig(load_in_8bit=True)
    processor = AutoProcessor.from_pretrained("HuggingFaceTB/SmolVLM-Instruct")
    model = AutoModelForVision2Seq.from_pretrained("HuggingFaceTB/SmolVLM-Instruct",
                                                    quantization_config=quantization_config)
    return model, processor

def load_gemini_model():
    #TODO: implement genai model
    pass