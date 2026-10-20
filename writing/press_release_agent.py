import os
import sys
# Add parent directory to path to import base_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent

class PressReleaseAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Press Release",
            system_instruction="You are a public relations specialist. Write professional, media-ready press releases following standard journalistic style and layouts."
        )

if __name__ == "__main__":
    agent = PressReleaseAgent()
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
