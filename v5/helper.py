import string

def relevance(query_embedding: list[float], memory_embedding: list[float]) -> float:

    score = similarity(query_embedding, memory_embedding)

    return score

def retreive_relevant(input_text: str, memory_store, index, num_shards: int, k=3):

    query_embedding = embed(input_text)

    shard_ids = shards_for_query(query_embedding, num_shards)

    candidate_memories = []

    for shard_id in shard_ids:

        for memory_id in index[shard_id]:

            memory = memory_store.get_by_id(memory_id)
            if memory is not None:
                candidate_memories.append(memory)

    scored = []

    for memory in candidate_memories:

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


def shard_for_embedding(embedding: list[float], num_shards: int) -> int:

    return int(abs(sum(embedding)) * 1000) % num_shards

def create_index(num_shards: int) -> dict[int, list[str]]:

    index = {}

    for shard_id in range(num_shards):
        index[shard_id] = []

    return index


def insert_into_index(index: dict[int, list[str]], memory_entry: dict, num_shards: int) -> None:

    shard_id = shard_for_embedding(memory_entry["embedding"], num_shards)
    index[shard_id].append(memory_entry["id"])

def shards_for_query(query_embedding: list[float], num_shards: int) -> list[int]:

    base = shard_for_embedding(query_embedding, num_shards)

    return [
        base,
        (base + 1) % num_shards,
        (base - 1) % num_shards
    ]
