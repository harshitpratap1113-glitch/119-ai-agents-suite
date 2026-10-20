import os
import sys
# Add parent directory to path to import base_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent

class FAQGeneratorAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="F A Q Generator",
            system_instruction="You are an FAQ writer. Generate a comprehensive list of frequently asked questions and clear, concise answers for a product or service."
        )

if __name__ == "__main__":
    agent = FAQGeneratorAgent()
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
