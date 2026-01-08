import nltk
import json
nltk.download("punkt")

from nltk import sent_tokenize

MAX_WORDS = 200

def chunk_text(text):
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = []

    word_count = 0
    for sent in sentences:
        words = sent.split()
        if word_count + len(words) > MAX_WORDS:
            chunks.append(" ".join(current_chunk))
            current_chunk=[]
            word_count=0
        current_chunk.append(sent)
        word_count += len(words)
    
    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

def build_corpus(wiki_articles):
    corpus = []
    for article in wiki_articles:
        text = article.get("text", "")
        if len(text) < 200:
            continue
        corpus.extend(chunk_text(text))
    return corpus