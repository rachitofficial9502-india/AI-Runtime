import string

def normalize(text: str) -> set[str]:

    output = set()

    lowercased = text.lower()

    splitted = lowercased.split(" ")

    translator = str.maketrans('', '', string.punctuation)

    for item in splitted:

        stripped = item.translate(translator)

        if len(stripped) < 3:

            continue

        output.add(stripped)

    return output

def relevance(input_text: str, memory_text: str) -> int:

    input_tokens = normalize(input_text)
    memory_tokens = normalize(memory_text)

    overlap = input_tokens.intersection(memory_tokens)
    return len(overlap)

def retreive_relevant(input_text: str, memory_store, k=3):

    scored = []

    for memory in memory_store.get_all():
        score = relevance(input_text, memory["content"])

        if score > 0:

            scored.append(memory, score)

    scored.sort(key=lambda x: x[1], reverse=True)

    top_memories = [m for m, _ in scored[:k]]

    return top_memories


# NOTE:
# This retrieval mechanism is intentionally naive.
# It relies on lexical token overlap and fails on semantic relevance.

