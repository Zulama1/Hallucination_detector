from Retrieval.retriever import Retriever

retriever = Retriever()
claim = "The Eiffel tower is located in Paris"
ret = retriever.retrieve(claim, 5)

for r in ret[:3]:
    print("-", r[:200])