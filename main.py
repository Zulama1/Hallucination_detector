from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from Pipeline.run_pipeline import run
model = SentenceTransformer("all-MiniLM-L6-v2")

