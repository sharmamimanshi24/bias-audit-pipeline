from openai import OpenAI

class RefinerAgent:
    def __init__(self):
        self.client = OpenAI(
            base_url="http://localhost:11434/v1",
            api_key="ollama"
        )
        self.model = "mistral-nemo"

    def run(self, state):
        print(f"[Refiner] Processing...")
        
        bias_info = state.audit_report
        is_biased = bias_info.get("bias_detected", False)

        if not is_biased:
            print("[Refiner] No bias detected. Passing original through.")
            state.refined_response = state.generated_response
            return state

        findings = bias_info.get('findings', [{}])
        first_finding = findings[0] if findings else {}

        refinement_prompt = f"""
        USER ORIGINAL QUERY: {state.user_query}
        ORIGINAL RESPONSE: {state.generated_response}
        
        AUDITOR FINDINGS:
        - Evidence: {first_finding.get('evidence', 'N/A')}
        - Suggested Correction: {first_finding.get('suggested_correction', 'Remove biased language')}

        Rewrite the ORIGINAL RESPONSE removing the bias. 
        Be neutral, inclusive and maintain accuracy.
        Just provide the corrected text.
        """

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a neutral, objective editor."},
                    {"role": "user", "content": refinement_prompt}
                ],
                temperature=0.3
            )
            
            state.refined_response = response.choices[0].message.content
            print("[Refiner] Done!")
            
        except Exception as e:
            print(f"[Refiner] Error: {e}")
            state.refined_response = state.generated_response
            
        return state
