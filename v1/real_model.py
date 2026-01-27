import config

from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=config.GEMINI_API_KEY)

class RealModel:

    def generate(self, prompt: str) -> str:

        content = prompt.split("<USER>")

        if len(content) < 2:
            return "I don't know."

        response = client.models.generate_content(
            model="gemini-3-flash-preview", contents=content
        )
        
        return response.text
