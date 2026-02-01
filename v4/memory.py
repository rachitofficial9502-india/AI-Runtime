import datetime
import config
from helper import embed

class MemoryStore:

    def __init__(self):
        
        self.memory = []
        self.next_id = 1

    def add(self, kind: str, content: str):

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

    def get(self, kind: str, limit: int | None = None):

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
    
    def get_all(self):

        return self.memory


                
    