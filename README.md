# Hallucination Detector

## Overview
Claim-level hallucination detection using retrieval-based verification on HaluEval(QA subset).

## Pipeline
- Claim Extraction
- Evidence Retrieval
- Claim Verification
- Claim-level Aggregation

## Tech Stack
- Python, PyTorch
- Sentence-Transformers
- Hugging Face Transformers (RoBERTa MNLI)
- HaluEval

## Evaluation
- Dataset: HaluEval (QA subset)
- Evidence: Gold knowledge provided in dataset
- Model: RoBERTa-large MNLI (zero-shot NLI)
- Evaluation size: 2,500 samples

### Metrics

| Metric    | Score |
|-----------|-------|
| Precision | 0.73  |
| Recall    | 0.80  |
| F1-score  | 0.77  |
| ROC-AUC   | 0.76  |

### Notes
- Higher recall indicates strong hallucination detection sensitivity.
- Evaluation was conducted on a subset due to computational constraints.
