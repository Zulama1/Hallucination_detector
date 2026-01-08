import json
import os
from Pipeline.claim_extraction import extract_claims

INPUT_PATH = "Data/raw/qa_data.json"
OUTPUT_PATH = "Data/processed/halu_eval_claims.json"

def normalize_label(label):
    if label is None:
        return 0
    
    if isinstance(label,str):
        return 1 if label.lower() in ["hallucinated", "yes", "true"] else 0
    return int(label)

def preprocess():
    os.makedirs("Data/processed", exist_ok=True)
    processed = []
    
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            line = line.strip()
            if not line:
                continue

            sample = json.loads(line)

            question = sample.get("question", "").strip()
            knowledge = sample.get("knowledge", "").strip()
            right_answer = sample.get("right_answer", "").strip()
            hallucinated_answer = sample.get("hallucinated_answer", "").strip()

            if not question:
                continue
            if right_answer:
                factual_claims = extract_claims(right_answer)

                if factual_claims:
                    processed.append({
                        "id": f"qa_{idx}_correct",
                        "knowledge": knowledge,
                        "question": question,
                        "answer": right_answer,
                        "claims": factual_claims,
                        "label": 0  # factual
                    })
            if hallucinated_answer:
                hallucinated_claims = extract_claims(hallucinated_answer)

                if hallucinated_claims:
                    processed.append({
                        "id": f"qa_{idx}_hallucinated",
                        "knowledge": knowledge,
                        "question": question,
                        "answer": hallucinated_answer,
                        "claims": hallucinated_claims,
                        "label": 1  # hallucinated
                    })
    
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(processed, f, indent=2)

    print(f"Processed {len(processed)} samples")


if __name__ == "__main__":
    preprocess()