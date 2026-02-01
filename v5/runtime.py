from context import Context
from real_model import RealModel
from memory import MemoryStore
from helper import retreive_relevant, create_index, insert_into_index
from config import NUM_SHARDS

class RunTime:

    def __init__(self):
        
        self.context = Context()
        self.model = RealModel()
        self.memory = MemoryStore()

        # Indexes are cached structure. Memory is durable state.
        self.initialize_index()

        self.context.add("system", "You are a helpful assistant.")

    def initialize_index(self):

        self.index = create_index(NUM_SHARDS)
        for memory in self.memory.get_all():
            insert_into_index(self.index, memory, NUM_SHARDS)

    def step(self, user_input: str) -> str:

        memory_blocks = []

        top_memories = retreive_relevant(user_input, self.memory, self.index, NUM_SHARDS)

        if top_memories:
            memory_blocks.append("PAST MEMORIES:")
            for memory in top_memories:
                memory_blocks.append(f"- {memory["kind"]} : {memory["content"]}")

        if memory_blocks:
            self.context.add("system", "\n".join(memory_blocks))
        
        self.context.add("user", user_input)

        prompt = self.context.build()

        response = self.model.generate(prompt)

        self.context.add("assistant", response)

        if "from now on" in response:
            self.memory.add("decision", response, self.index, NUM_SHARDS)

        return response
    

