from byaldi import RAGMultiModalModel

def load_rag_model():
    model = RAGMultiModalModel.from_index("reports", device="cpu")
    return model
