import os
import sys

# Add parent directory to path to import base_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent

class SqlQueryGeneratorAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Natural English to SQL Query Writer",
            system_instruction="You are an expert database administrator. Your job is to translate natural English questions about data into correct, optimized, and executable SQL queries."
        )

if __name__ == "__main__":
    agent = SqlQueryGeneratorAgent()
    print("="*50)
    print(f"Running {agent.name}...")
    print("="*50)
    user_prompt = input("Enter your request: ").strip()
    
    print("\nProcessing request...")
    response = agent.run(user_prompt)
    print("\n[Response]:")
    print(response)
