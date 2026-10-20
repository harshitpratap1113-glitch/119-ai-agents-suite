import os
import sys

# Add parent directory to path to import base_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent

class DigitalDeclutterAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Digital Declutter Guide",
            system_instruction="You are a digital organization advisor. Your job is to look at listings of user files, folders, or temporary directories, and suggest items to delete, archive, or organize to reclaim storage."
        )

if __name__ == "__main__":
    agent = DigitalDeclutterAgent()
    print("="*50)
    print(f"Running {agent.name}...")
    print("="*50)
    user_prompt = input("Enter your request: ").strip()
    
    print("\nProcessing request...")
    response = agent.run(user_prompt)
    print("\n[Response]:")
    print(response)
