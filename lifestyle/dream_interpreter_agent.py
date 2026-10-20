import os
import sys
# Add parent directory to path to import base_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent

class DreamInterpreterAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Dream Interpreter",
            system_instruction="You are a symbolic dream interpreter. Analyze dream descriptions and explore traditional, psychological, or archetypal interpretations."
        )

if __name__ == "__main__":
    agent = DreamInterpreterAgent()
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
