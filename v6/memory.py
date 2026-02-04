import datetime
import config
from helper import embed, insert_into_index
import json
import os

class MemoryStore:

    def __init__(self):
        
        self.memory = []
        self.next_id = 1

        if os.path.exists("memory.jsonl"):

            with open("memory.jsonl", "r") as f:

                for line in f:

                    entry = json.loads(line)
                    self.memory.append(entry)
                    self.next_id = max(self.next_id, entry['id'] + 1)

    def add(self, kind: str, content: str, index, num_shards: int):

        if kind not in config.ALLOWED_KINDS:
            raise ValueError(f"Kind not in allowed kinds: {kind}")

        memory_entry = {
            "id": self.next_id,
            "kind": kind,
            "content": content,
            "embedding": embed(content),
            "timestamp": datetime.datetime.now().isoformat()
        }

        self.memory.append(memory_entry)
        self.next_id += 1

        with open("memory.jsonl", "a") as f:
            f.write(json.dumps(memory_entry) + "\n")

        insert_into_index(index, memory_entry, num_shards)

    def get_by_kind(self, kind, limit: int | None = None):

        output = []

        iterable = (
            reversed(self.memory)
            if limit is None
            else reversed(self.memory[-limit:])
        )

        for entry in iterable:

            if entry["kind"] == kind:

                output.append(entry)

        return output
    
    def get_by_id(self, memory_id: int):

        for entry in self.memory:

            if entry['id'] == memory_id:

                return entry
            
        return None
    
    def get_all(self):

        return self.memory


                
    