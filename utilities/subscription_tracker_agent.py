import os
import sys

# Add parent directory to path to import base_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent

class SubscriptionTrackerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Subscription and Free Trial Tracker",
            system_instruction="You are a personal finance assistant. Your job is to analyze lists of recurring bills, software subscriptions, or free trials and suggest optimal billing cycles, alerts, or cancellations."
        )

if __name__ == "__main__":
    agent = SubscriptionTrackerAgent()
    print("="*50)
    print(f"Running {agent.name}...")
    print("="*50)
    user_prompt = input("Enter your request: ").strip()
    
    print("\nProcessing request...")
    response = agent.run(user_prompt)
    print("\n[Response]:")
    print(response)
