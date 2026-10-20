import os
import sys

# Add parent directory to path to import base_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent

class LegacyRefactorerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Legacy Code Refactorer",
            system_instruction="You are an expert AI software engineer. Your job is to analyze legacy code and refactor it into clean, modern, and efficient code using the latest language standards."
        )

if __name__ == "__main__":
    agent = LegacyRefactorerAgent()
    print("="*50)
    print(f"Running {agent.name}...")
    print("="*50)
    user_prompt = input("Enter your request: ").strip()
    
    print("\nProcessing request...")
    response = agent.run(user_prompt)
    print("\n[Response]:")
    print(response)
