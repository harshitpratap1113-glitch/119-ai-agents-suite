import os
import sys
# Add parent directory to path to import base_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent

class Base64EncoderAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Base64 Encoder",
            system_instruction="You are a Base64 encoding/decoding helper. Convert strings and binary representations into Base64 formats and explain the math."
        )

if __name__ == "__main__":
    agent = Base64EncoderAgent()
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
