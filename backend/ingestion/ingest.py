# the script will ingest the pdf from a folder and create the index to be load later by RAG apps. 

import argparse
from byaldi import RAGMultiModalModel


RETRIEVAL_MODAL_NAME="vidore/colpali"


class Ingester():
    def __init__(self, modal_name):
        self.RAG: RAGMultiModalModel = RAGMultiModalModel.from_pretrained(pretrained_model_name_or_path=modal_name)
        self.index_name = "reports"
        print(f" started ingestion in location : {self.index_name}")
        
        
    def ingest_pdfs(self, input_file_path) -> None:
        self.RAG.index(
            input_path=input_file_path, # The path to your documents
            index_name=self.index_name, # It'll be saved at `index_root/index_name/`.
            store_collection_with_index=True, # store the base64 encoded documents. : less work in api 
            overwrite=True #overwrite everytime when running the ingestion 
        )
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-path", "--path", required=True, help="pdf paths for ingestion")
    parser.add_argument("-model", "--model", required=False, help= "model to use in ingestion pipeline")
    args = parser.parse_args()
    i = Ingester(RETRIEVAL_MODAL_NAME)
    i.ingest_pdfs(args.path)
    print(f" successfully completed : {i.index_name}")