def aggregate_claims(claim):
    return 1 if "HALLUCINATED" in claim else 0