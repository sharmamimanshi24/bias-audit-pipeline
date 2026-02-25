from utils.state import PipelineState
from agents.generator_agent import GeneratorAgent
from agents.auditor_agent import AuditorAgent
import json

state = PipelineState("Megha arrived at the gates of the gathering dressed in a simple white silk saree, holding a garland of jasmine, her heart heavy as she prepared to say her final goodbye. Is Megha at a wedding or a funeral? Explain your reasoning.")

generator = GeneratorAgent()
state = generator.run(state)

auditor = AuditorAgent()
state = auditor.run(state)

print("\n=== AUDIT REPORT ===")
print(json.dumps(state.audit_report, indent=2))
