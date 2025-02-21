# PPTRag
A complete offline, local multi modal RAG system. 

# Installation 

### Using Docker
This is experimental.

```
docker compose up --build
```

or 

### Install UV , pnpm and its dependencies
1. Install uv based on its recommended version: https://docs.astral.sh/uv/getting-started/installation/
2. Install node and pnpm
### Usage

```
pnpm install # install dependencies
pnpm run dev # running frontend UI
```

```
uv sync # install dependencies
uv run fastapi dev # running backend service
```

### Data Ingestion
1. Either use the ingestion pipeline 
```
python ingestion/ingest.py --path ./data/pdf    
```
*reports collections will be made for byaldi using the colpali model. The process will take around 10/15 mins. 

2. Or Download the zip and put it in the backend folder as .byaldi folder

```
https://drive.google.com/file/d/1eA1tGJQQJjKJmYToEapYhA918lNnSCb1/view?usp=sharing
```



### V1
#### Frontend
![chat ui](docs/imgs/v1-frontend.png)

#### Backend
![backend](docs/imgs/v1-backend.png)


### Notes

1. [Development Timeline](https://github.com/shekharkoirala/PPTRag/blob/main/changelog.md)
2. My first recommendation is to use [Milvus](https://milvus.io/) as vector storage ( best for production settings as well. ) Here [Byaldi](https://github.com/AnswerDotAI/byaldi) is used due to two main reason
a. It has clean rag pipeline.
b. It works with both CPU/GPU ( this is my main reason.)
3. Rag system contains Retriever and the generator
a. Retriever: byaldi is used as data are preprocessed and loaded in CPU as vectors. 
b. Generator: As the system is multi-modal, smolVlm model is used for the generation task. 