### [2025/02/20]
started 10 days later, lets complete this project. 



### [2025/02/10]
will use [gemini model](https://github.com/googleapis/python-genai/releases) 
This will substantially improve the generation part, I might send more images. 
On top of that, Gemini api free tier limits:
```
10 RPM (requests per minute)
10,000 TPM (tokens per minute)
1,000 RPD (requests per day)
```


### [2025/02/09]

I am thinking to use vllm instead of llama parse to get the data. I already know tools like https://www.eyelevel.ai/, where we can extract the images and use any vision model to extract the embeddings. This would be complex and expensive to code. 
I found the paper published at 6 feb 2025: [ColPali: EFFICIENT DOCUMENT RETRIEVAL WITH VISION LANGUAGE MODELS](https://arxiv.org/pdf/2407.01449)

I want to use the local gpu (8 gb : 1070 ). I am choosing not use any cloud provider as it might cost me some money.
indexing is done using GPU as a seperate process. It took 12 mins to process the pdfs, 204 images. 
The retrieval model ( COLPALI) runs in CPU, it takes around 3-5 secs for each query to get topk=2 images from the data. 
The generation models ( SMOLVLLM) run in GPU, it takes around 10-100 secs for the generating the text output. 

sample query:
```{
  "query": "what are the conocoPhillips Commercial Advantage, list them down."
}
```
sample result:

```
{
  "results": "User:<image>what are the conocoPhillips Commercial Advantage, list them down.\nAssistant: The conocoPhillips Commercial Advantage includes:\n- Port Arthur LNG Marketing Example: Sale into Germany\n- Global Marketing Presence: >10 BCFD and >1 MMBOD1\n- 9x Equity\n- 6.0 GWh\n- 1 MTPA\n- 113 MTPA\n- 2nd Largest\n- Utilizing Optimized Global LNG\n- Cascade® Process technology provider\n- 25 Cargoes\n- 45%\n- 180 MBOD\n- 25 Cargoes\n- 45%\n- 180 MBOD\n- 25 Cargoes\n- 45%\n- 180 MBOD\n- 25 Cargoes\n- 45%\n- 180 MBOD\n- 25 Cargoes\n- 45%\n- 180 MBOD\n- 25 Cargoes\n- 45%\n- 180 MBOD\n- 25 Cargoes\n- 45%\n- 180 MBOD\n- 25 Cargoes\n- 45%\n- 180 MBOD\n- 25 Cargoes\n- 45%\n- 180 MBOD\n- 25 Cargoes\n- 45%\n- 180 MBOD\n- 25 Cargoes\n- 45%\n- 180 MBOD\n- 25 Cargoes\n- 45%\n- 180 MBOD\n- 25 Cargoes\n- 45%\n- 180 MBOD\n- 25 Cargoes\n- 45%\n- 180 MBOD\n- 25 Cargoes\n- 45%\n- 180 MBOD\n- 25 Cargoes\n- 45%\n- 180 MBOD\n- 25 Cargoes\n- 45%\n- 180 MBOD\n- 25 Cargoes\n- 45%\n- 180 MBOD\n- 25 Cargoes\n- 45%"
}
```

feedback:
I would test with other generation model, it should perform alot better. 
for the task, might need to focus on different things as frontend will be tested too. 


### [2025/02/08]

Tried Multiple Extraction tools from the pdf. The provided pdfs file capture the real world scenario as 2023's version are alll images. 
I have tried pdfplumber, hotpdf, tessaract , unstructured, llama parse, pymupdf, pymupdf4llm etc. 
Only unstructured and llama-parse could able to parse data from 2023's pdf. 
for 2024's pdf, the pdf should be splitted into three part to be inside the free quota of lllama parse. 
I will try to use llama parse for both of the document as it is the most accurate representation of data. 

### [2025/02/07]

General setup of repo: Will work 1/2 hr per day let' see. 