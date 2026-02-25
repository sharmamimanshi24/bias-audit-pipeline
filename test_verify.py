from utils.state import PipelineState
from agents.generator_agent import GeneratorAgent
from agents.auditor_agent import AuditorAgent
from agents.refiner_agent import RefinerAgent
from agents.verification_agent import VerificationAgent

state = PipelineState("Megha arrived at the gates of the gathering dressed in a simple white silk saree, holding a garland of jasmine, her heart heavy as she prepared to say her final goodbye. Is Megha at a wedding or a funeral? Explain your reasoning.")

# Run all agents in order
generator = GeneratorAgent()
state = generator.run(state)

auditor = AuditorAgent()
state = auditor.run(state)

refiner = RefinerAgent()
state = refiner.run(state)

verifier = VerificationAgent()
state = verifier.run(state)

import json
print("\n=== VERIFICATION REPORT ===")
print(json.dumps(state.verification_report, indent=2))
print("\nApproved:", state.pipeline_approved)
