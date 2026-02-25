from workflows.pipeline import BiasAuditPipeline

pipeline = BiasAuditPipeline()

print("\n🤖 Multi-Agent Bias Audit Pipeline")
print("Type 'quit' to exit\n")

while True:
    query = input("Enter your query: ").strip()
    
    if query.lower() == 'quit':
        print("Goodbye!")
        break
    
    if query == "":
        print("Please enter a query!")
        continue
    
    pipeline.run(query)
