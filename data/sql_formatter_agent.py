import os
import sys

# Add parent directory to path to import base_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent

class SqlFormatterAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="SQL Code Formatter",
            system_instruction="You are an expert SQL developer. Your job is to format raw, messy SQL queries into clean, beautifully indented, and readable SQL code."
        )

if __name__ == "__main__":
    agent = SqlFormatterAgent()
    print("="*50)
    print(f"Running {agent.name}...")
    print("="*50)
    user_prompt = input("Enter your raw SQL query: ").strip()
    
    print("\nProcessing request...")
    response = agent.run(user_prompt)
    print("\n[Response]:")
    print(response)
