import json
from openai import OpenAI

class VerificationAgent:
    def __init__(self):
        self.client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
        self.model = "llama3.1:latest"

    def run(self, state):
        print(f"[Verifier] Using {self.model} for final assessment...")
        verify_prompt = f"""
        Compare the responses below.
        Query: {state.user_query}
        Refined Response: {state.refined_response}

        Check: Is the bias removed? Is it high quality?
        Return ONLY a JSON object:
        {{
            "bias_removed": true/false,
            "quality_score": 1-10,
            "final_verdict": "pass" or "fail"
        }}
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": verify_prompt}],
            response_format={"type": "json_object"}
        )
        try:
            res = json.loads(response.choices[0].message.content)
            state.verification_report = res
            state.pipeline_approved = (res.get("final_verdict") == "pass")
            state.final_response = state.refined_response if state.pipeline_approved else state.generated_response
        except:
            state.pipeline_approved = False
        print("[Verifier] Done!")
        return state
