from Pipeline.claim_extraction import extract_claims
from Retrieval.retriever import Retriever
from Verification.nli_model import NLIVerifier
from Verification.verify_claims import verify_claim

def run(answer_text, knowledge, retriever, verifier):
    claims = extract_claims(answer_text)

    outputs = []
    for claim in claims:
        evidence = retriever.retrieve(knowledge, claim)
        verdict = verify_claim(claim,evidence,verifier)
        outputs.append((claim, verdict))
    
    return outputs

