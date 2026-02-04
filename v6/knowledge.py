import os
import json
from helper import embed, insert_into_index, create_index, shards_for_query, similarity
import config

class KnowledgeStore:

    def __init__(self):
        
        self.knowledge = []
        self.next_id = 1

        self.index = create_index(config.NUM_SHARDS)

        if os.path.exists("knowledge.jsonl"):

            with open("knowledge.jsonl", "r") as f:

                for line in f:

                    entry = json.loads(line)
                    self.knowledge.append(entry)
                    self.next_id = max(self.next_id, entry['id'] + 1)

                    insert_into_index(self.index, entry, config.NUM_SHARDS)
            

    def add(self, source: str, content: str):

        knowledge_entry = {
            "id": self.next_id,
            "source": source,
            "content": content,
            "embedding": embed(content) 
        }

        self.knowledge.append(knowledge_entry)
        self.next_id += 1

        with open("knowledge.jsonl", "a") as f:

            f.write(json.dumps(knowledge_entry) + "\n")

        insert_into_index(self.index, knowledge_entry, config.NUM_SHARDS)


    def get_all(self):

        return self.knowledge
    
    def get_by_id(self, knowledge_id: int):

        for entry in self.knowledge:

            if entry["id"] == knowledge_id:

                return entry
        
        return None
    
    def retrieve(self, query: str, k:int = 3):

        query_embedding = embed(query)

        shard_ids = shards_for_query(query_embedding, config.NUM_SHARDS)

        candidate_knowledge = []

        for shard_id in shard_ids:

            for knowledge_id in self.index[shard_id]:

                entry = self.get_by_id(knowledge_id)
                if entry is not None:
                    candidate_knowledge.append(entry)

        scored = []

        for entry in candidate_knowledge:

            score = similarity(query_embedding, entry["embedding"])

            scored.append((entry, score))

        scored.sort(key= lambda x: x[1], reverse=True)

        top_entries = [m for m, _ in scored[:k]]

        return top_entries




    
