import json
from openai import OpenAI
from policies.ethics_policy import ETHICS_POLICY

class AuditorAgent:
    def __init__(self):
        self.client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
        self.model = "llama3.1:latest"

    def run(self, state):
        print(f"[Auditor] Using {self.model} to detect bias...")
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": ETHICS_POLICY},
                {"role": "user", "content": f"Audit this text for bias:\n\n{state.generated_response}"}
            ],
            response_format={"type": "json_object"}
        )
        raw = response.choices[0].message.content
        try:
            clean = raw.strip().replace("```json", "").replace("```", "").strip()
            state.audit_report = json.loads(clean)
        except:
            state.audit_report = {"bias_detected": True, "raw": raw}
        print("[Auditor] Done!")
        return state
