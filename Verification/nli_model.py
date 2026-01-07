from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

class NLIVerifier:
    def __init__(self):
        self.tokenizer =  AutoTokenizer.from_pretrained(
            "roberta-large-mnli"
        )
        self.model = AutoModelForSequenceClassification.from_pretrained(
            "roberta-large-mnli"
        )

    def verify(self, premise, hypothesis):
        inputs = self.tokenizer(
            premise, hypothesis, return_tensors = 'pt', truncation = True
        )
        with torch.no_grad():
            logits = self.model(**inputs). logits
        probs = torch.softmax(logits, dim=-1)[0]
        labels = ["CONTRADICTION", "NEUTRAL", "ENTAILMENT"]
        return labels[probs.argmax().item()]