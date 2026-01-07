import faiss
import pickle
from sentence_transformers import SentenceTransformer

class Retriever:
    def __init__(self):
        self.model = SentenceTransformer("all-mpnet-base-v2")
        self.index = faiss.read_index("data/processed/wiki.index")
        self.docs = pickle.load(open("data/processed/wiki_docs.pkl", "rb"))

    def retrieve(self, claim, k=5):
        emb = self.model.encode([claim])
        distances, indices = self.index.search(emb,k)
        return [self.docs[i] for i in indices[0]]
    
    