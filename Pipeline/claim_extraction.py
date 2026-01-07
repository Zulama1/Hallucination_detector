import nltk
nltk.download('punkt')

from nltk.tokenize import sent_tokenize

def extract_claims(text: str):
    claims = sent_tokenize(text)
    return [c.strip() for c in claims if len(c.strip())> 5]


