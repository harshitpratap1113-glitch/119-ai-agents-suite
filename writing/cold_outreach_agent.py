import os
import sys

# Add parent directory to path to import base_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent

class ColdOutreachAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Cold Outreach Pitch Writer",
            system_instruction="You are a professional copywriter and sales expert. Your job is to write highly personalized, conversion-optimized B2B cold email pitches or LinkedIn connection messages."
        )

if __name__ == "__main__":
    agent = ColdOutreachAgent()
    print("="*50)
    print(f"Running {agent.name}...")
    print("="*50)
    user_prompt = input("Enter your request: ").strip()
    
    print("\nProcessing request...")
    response = agent.run(user_prompt)
    print("\n[Response]:")
    print(response)
