import os
import sys
# Add parent directory to path to import base_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent

class AdventureGameAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Adventure Game",
            system_instruction="You are a Text-based Adventure Game Master. Guide the user through interactive stories where their choices determine the outcome."
        )

if __name__ == "__main__":
    agent = AdventureGameAgent()
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
