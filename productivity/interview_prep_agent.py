import os
import sys
# Add parent directory to path to import base_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent

class InterviewPrepAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Interview Prep",
            system_instruction="You are an interview preparation coach. Generate role-specific behavioral and technical interview questions, with STAR-method answer guides."
        )

if __name__ == "__main__":
    agent = InterviewPrepAgent()
    if len(sys.argv) > 1:
        prompt = " ".join(sys.argv[1:])
    else:
        prompt = input("Enter prompt for " + agent.name + ": ")
    
    print("\n" + "="*50)
    print("Running " + agent.name + "...")
    print("="*50)
    
    result = agent.run(prompt)
    print("\n[Response]:")
    print(result)
