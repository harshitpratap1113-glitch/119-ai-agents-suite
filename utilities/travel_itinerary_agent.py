import os
import sys

# Add parent directory to path to import base_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent

class TravelItineraryAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Travel Vacation Itinerary Planner",
            system_instruction="You are a travel coordinator. Your job is to create a detailed day-by-day vacation itinerary including flights, hotel choices, restaurants, and sightseeing spots based on budget and duration."
        )

if __name__ == "__main__":
    agent = TravelItineraryAgent()
    print("="*50)
    print(f"Running {agent.name}...")
    print("="*50)
    user_prompt = input("Enter your request: ").strip()
    
    print("\nProcessing request...")
    response = agent.run(user_prompt)
    print("\n[Response]:")
    print(response)
