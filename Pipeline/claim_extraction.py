import nltk
nltk.download('punkt_tab')

from nltk.tokenize import sent_tokenize

def extract_claims(text: str):
    text = text.strip()
    if len(text.split()) <= 3:
        return[text]
    
    claims = sent_tokenize(text)
    return [c.strip() for c in claims if len(c.strip())> 3]



