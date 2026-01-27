class Context:

    def __init__(self):

        self.messages = []

    def add(self, role, content):

        message = {
            "role": role,
            "content": content}
        self.messages.append(message)

    def build(self):
        
        output = ""

        for message in self.messages:

            role = message["role"].upper()
            content = message["content"]

            output += f"<{role}>\n"
            output += f"{content}\n"
            output += f"</{role}>\n\n"

        return output
        


            
    
