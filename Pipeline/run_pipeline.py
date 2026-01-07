from Pipeline.claim_extraction import extract_claims
from Retrieval.retriever import Retriever
from Verification.nli_model import NLIVerifier
from Verification.verify_claims import verify_claim

def run(answer_text):
    claims = extract_claims(answer_text)
    retriever = Retriever()
    verifier = NLIVerifier()

    outputs = []
    for claim in claims:
        evidence = retriever.retrieve(claim)
        verdict = verify_claim(claim,evidence,verifier)
        outputs.append(verdict)
    
    return outputs

