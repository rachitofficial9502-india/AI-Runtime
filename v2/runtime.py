from context import Context
from real_model import RealModel
from memory import MemoryStore

class RunTime:

    def __init__(self):
        
        self.context = Context()
        self.model = RealModel()
        self.memory = MemoryStore()
        self.context.add("system", "You are a helpful assistant.")

    def step(self, user_input: str) -> str:

        memory_blocks = []

        decisions = self.memory.get("decision", 3)
        constraints = self.memory.get("constraint")

        if decisions:
            memory_blocks.append("PAST DECISIONS:")
            for decision in decisions:
                memory_blocks.append(f"- {decision["content"]}")
        if constraints:
            memory_blocks.append("CONSTRAINTS:")
            for constraint in constraints:
                memory_blocks.append(f"-  {constraint["content"]}")

        if memory_blocks:
            self.context.add("system", "\n".join(memory_blocks))
        
        self.context.add("user", user_input)

        prompt = self.context.build()

        response = self.model.generate(prompt)

        self.context.add("assistant", response)

        if "from now on" in response:
            self.memory.add("decision", response)

        return response
    

