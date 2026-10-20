import os
import sys

# Add parent directory to path to import base_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent

class CalendarTimeBlockerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Calendar Time Blocker",
            system_instruction="You are a personal efficiency assistant. Your job is to take a list of tasks, priorities, and deadlines, and block out an optimized, hour-by-hour daily calendar schedule."
        )

if __name__ == "__main__":
    agent = CalendarTimeBlockerAgent()
    print("="*50)
    print(f"Running {agent.name}...")
    print("="*50)
    user_prompt = input("Enter your request: ").strip()
    
    print("\nProcessing request...")
    response = agent.run(user_prompt)
    print("\n[Response]:")
    print(response)
