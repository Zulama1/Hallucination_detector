def verify_claim(claim, evidence_list, verifier):
    results = []
    for evidence in evidence_list:
        label = verifier.verify(evidence, claim)
        results.append(label)
    
    if 'CONTRADICTION' in results:
        return 'HALLUCINATED'
    if all(r== 'NEUTRAL' for r in results):
        return 'HALLUCINATED'
    return 'FACTUAL'