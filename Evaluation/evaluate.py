import json
from Pipeline.run_pipeline import run
from Evaluation.aggregation import aggregate_claims
from Evaluation.metrics import compute_metrics

DATA_PATH = "data/processed/halu_eval_claims.json"

def evaluate():
    data = json.load(open(DATA_PATH))
    
    y_true = []
    y_pred = []

    for sample in data:
        answer = sample["answer"]
        true_label = sample["label"]
        knowledge = sample["knowledge"]
        results = run(answer, knowledge)
        
        claim_verdicts = [v for _, v in results]

        pred_label = aggregate_claims(claim_verdicts)

        y_true.append(true_label)
        y_pred.append(pred_label)

    metrics = compute_metrics(y_true, y_pred)
    print(metrics)

if __name__ == "__main__":
    evaluate()
