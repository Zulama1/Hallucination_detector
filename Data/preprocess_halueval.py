import json
from Pipeline.claim_extraction import extract_claims

INPUT_PATH = "Data/raw/qa_data.json"
OUTPUT_PATH = "Data/processed/halu_eval_claims.json"

def normalize_label(label):
    if isinstance(label,str):
        return 1 if label.lower() in ["hallucinated", "yes", "true"] else 0
    return int(label)

def preprocess():
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    processed = []
    for idx, sample in enumerate(data):
        answer = sample.get("answer", "")