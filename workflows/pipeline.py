from agents.generator_agent import GeneratorAgent
from agents.auditor_agent import AuditorAgent
from agents.refiner_agent import RefinerAgent
from agents.verification_agent import VerificationAgent
from utils.state import PipelineState
import json
import os

class BiasAuditPipeline:
    def __init__(self):
        print("Initializing pipeline...")
        self.generator = GeneratorAgent()
        self.auditor = AuditorAgent()
        self.refiner = RefinerAgent()
        self.verifier = VerificationAgent()
        print("All agents ready!")

    def run(self, query):
        # Create shared state
        state = PipelineState(query)
        
        print(f"\n{'='*50}")
        print(f"Run ID: {state.run_id}")
        print(f"Query: {query}")
        print(f"{'='*50}")

        # Run all 4 agents in sequence
        state = self.generator.run(state)
        state = self.auditor.run(state)
        state = self.refiner.run(state)
        state = self.verifier.run(state)

        # Save transparency log
        self.save_log(state)

        # Print final summary
        self.print_summary(state)

        return state

    def print_summary(self, state):
        print(f"\n{'='*50}")
        print("PIPELINE COMPLETE")
        print(f"{'='*50}")
        print(f"\nORIGINAL RESPONSE:\n{state.generated_response}")
        print(f"\nBIAS DETECTED: {state.audit_report.get('bias_detected')}")
        print(f"SEVERITY: {state.audit_report.get('overall_severity')}")
        print(f"\nREFINED RESPONSE:\n{state.refined_response}")
        print(f"\nAPPROVED: {state.pipeline_approved}")
        print(f"QUALITY SCORE: {state.verification_report.get('quality_score')}")

    def save_log(self, state):
        os.makedirs("logs", exist_ok=True)
        log_path = f"logs/{state.run_id}.json"
        with open(log_path, "w") as f:
            json.dump({
                "run_id": state.run_id,
                "query": state.user_query,
                "generated": state.generated_response,
                "audit": state.audit_report,
                "refined": state.refined_response,
                "verification": state.verification_report,
                "approved": state.pipeline_approved
            }, f, indent=2)
        print(f"\nLog saved: {log_path}")
