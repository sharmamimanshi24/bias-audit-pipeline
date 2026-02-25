#This is the memory bank for our pipeline. 
# In a complex AI system, you don't just want a single answer; you want to track how that answer changes as it passes through different "Agents" (the Generator, the Auditor, the Refiner). 
# This class, PipelineState, holds all that information in one place.


import time

class PipelineState:
    def __init__(self, user_query):
        self.user_query = user_query
        self.run_id = f"run_{int(time.time())}"
        
        # Each agent will fill these in
        self.generated_response = None
        self.audit_report = None
        self.refined_response = None
        self.verification_report = None
        
        # Final output
        self.final_response = None
        self.pipeline_approved = False
    
    def show(self):
        print(f"\n Run ID: {self.run_id}")
        print(f" Query: {self.user_query}")
        print(f" Generated: {self.generated_response}")
        print(f" Audit: {self.audit_report}")
        print(f" Refined: {self.refined_response}")
        print(f" Verified: {self.verification_report}")
        print(f" Approved: {self.pipeline_approved}")