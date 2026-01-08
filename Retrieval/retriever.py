from nltk.tokenize import sent_tokenize

class Retriever:
    def __init__(self):
        pass

    def retrieve(self, knowledge, claim, k=3):
        """
        Returns top-k sentences from knowledge.
        """
        sentences = sent_tokenize(knowledge)
        return sentences[:k]
    
    