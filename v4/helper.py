import string

def relevance(query_embedding: list[float], memory_embedding: list[float]) -> float:

    score = similarity(query_embedding, memory_embedding)

    return score

def retreive_relevant(input_text: str, memory_store, k=3):

    scored = []

    query_embedding = embed(input_text)

    for memory in memory_store.get_all():

        score = relevance(query_embedding, memory["embedding"])

        scored.append((memory, score))

    scored.sort(key=lambda x: x[1], reverse=True)

    top_memories = [m for m, _ in scored[:k]]

    return top_memories

def embed(text: str) -> list[float]:

    ...

def similarity(query_embedding: list[float], memory_embedding: list[float]) -> float:

    ...

    # score = cosine_similarity(query_embedding, memory_embedding)

    # if normalized -> score = dot(query_embedding, memory_embedding)

    # return score



