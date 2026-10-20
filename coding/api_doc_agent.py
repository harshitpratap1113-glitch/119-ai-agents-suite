import os
import sys
# Add parent directory to path to import base_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent

class APIDocAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="A P I  Doc",
            system_instruction="You are an API documentation generator agent. Take API route definitions (Express, FastAPI, Flask, etc.) and generate clean OpenAPI/Swagger specifications or Markdown documentation."
        )

if __name__ == "__main__":
    agent = APIDocAgent()
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
