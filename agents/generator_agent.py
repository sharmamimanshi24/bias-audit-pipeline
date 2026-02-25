from openai import OpenAI

class GeneratorAgent:
    def __init__(self):
        self.client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
        self.model = "gemma3:1b"

    def run(self, state):
        print(f"[Generator] Using {self.model} to generate initial response...")
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Provide a complete and detailed response."},
                {"role": "user", "content": state.user_query}
            ]
        )
        state.generated_response = response.choices[0].message.content
        print("[Generator] Done!")
        return state
