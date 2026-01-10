import json
from Pipeline.run_pipeline import run
from Evaluation.aggregation import aggregate_claims
from Evaluation.metrics import compute_metrics
from Retrieval.retriever import Retriever
from Verification.nli_model import NLIVerifier

DATA_PATH = "data/processed/halu_eval_claims.json"
MAX_SAMPLES = 2500
def evaluate():
    data = json.load(open(DATA_PATH))
    data = data[:MAX_SAMPLES]

    retriever = Retriever()
    verifier = NLIVerifier()

    y_true = []
    y_pred = []


    for i, sample in enumerate(data):
        if i%50 == 0:
            print(f"Processed {i}/{len(data)} samples")

        answer = sample["answer"]
        true_label = sample["label"]
        knowledge = sample["knowledge"]

        results = run(
            answer, 
            knowledge, 
            retriever, 
            verifier)
        
        claim_verdicts = [v for _, v in results]
        pred_label = aggregate_claims(claim_verdicts)

        y_true.append(true_label)
        y_pred.append(pred_label)

    metrics = compute_metrics(y_true, y_pred)
    print("\nFinal metrics:")
    print(metrics)

if __name__ == "__main__":
    evaluate()
