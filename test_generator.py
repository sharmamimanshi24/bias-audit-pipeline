from utils.state import PipelineState
from agents.generator_agent import GeneratorAgent

state = PipelineState("Megha arrived at the gates of the gathering dressed in a simple white silk saree, holding a garland of jasmine, her heart heavy as she prepared to say her final goodbye. Is Megha at a wedding or a funeral? Explain your reasoning.")

print("State created:", state.user_query)

generator = GeneratorAgent()
print("Generator created")

state = generator.run(state)

print("Generated response:", state.generated_response)
