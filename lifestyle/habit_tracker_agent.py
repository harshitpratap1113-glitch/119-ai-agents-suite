import os
import sys
# Add parent directory to path to import base_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent

class HabitTrackerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Habit Tracker",
            system_instruction="You are a habit formation coach. Provide tips, reminders, and psychological strategies to help the user build positive habits and break bad ones."
        )

if __name__ == "__main__":
    agent = HabitTrackerAgent()
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
