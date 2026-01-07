import faiss
import pickle
from sentence_transformers import SentenceTransformer

def faiss_build_extractor(documents):
    model = SentenceTransformer('all-mpnet-base-v2')
    embeddings = model.encode(documents, show_progress_bar=True)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    faiss.write_index(index, "data/processed/wiki.index")
    pickle.dump(documents, open("data/processed/wiki_docs.pkl", "wb"))