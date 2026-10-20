import os
import sys

# Add parent directory to path to import base_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent

class EnvSetupGuardAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Environment Setup Guard",
            system_instruction="You are an expert devops and setup helper. Your job is to inspect project dependencies (like requirements.txt, package.json, etc.) and generate a clear, step-by-step local development setup guide."
        )

if __name__ == "__main__":
    agent = EnvSetupGuardAgent()
    print("="*50)
    print(f"Running {agent.name}...")
    print("="*50)
    user_prompt = input("Enter your request: ").strip()
    
    print("\nProcessing request...")
    response = agent.run(user_prompt)
    print("\n[Response]:")
    print(response)
