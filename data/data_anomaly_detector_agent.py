import os
import sys

# Add parent directory to path to import base_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent

class DataAnomalyDetectorAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Data Anomaly and Outlier Spotter",
            system_instruction="You are a data quality analyst. Your job is to scan table summaries, CSV dumps, or Excel sheets to identify outliers, formatting discrepancies, or potential data entry errors."
        )

if __name__ == "__main__":
    agent = DataAnomalyDetectorAgent()
    print("="*50)
    print(f"Running {agent.name}...")
    print("="*50)
    user_prompt = input("Enter your request: ").strip()
    
    print("\nProcessing request...")
    response = agent.run(user_prompt)
    print("\n[Response]:")
    print(response)
