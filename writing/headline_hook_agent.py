import os
import sys
# Add parent directory to path to import base_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent

class HeadlineHookAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Headline Hook",
            system_instruction="You are a headline and hook generator. Create attention-grabbing headlines, video titles, or email subject lines designed for high click-through rates."
        )

if __name__ == "__main__":
    agent = HeadlineHookAgent()
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
