import os
import sys

# Add parent directory to path to import base_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent

class MealPrepPlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Personal Meal Prep Planner",
            system_instruction="You are a nutritionist and meal planner. Your job is to generate a weekly meal prep plan and detailed grocery checklist based on user dietary needs, calorie targets, and preferences."
        )

if __name__ == "__main__":
    agent = MealPrepPlannerAgent()
    print("="*50)
    print(f"Running {agent.name}...")
    print("="*50)
    user_prompt = input("Enter your request: ").strip()
    
    print("\nProcessing request...")
    response = agent.run(user_prompt)
    print("\n[Response]:")
    print(response)
