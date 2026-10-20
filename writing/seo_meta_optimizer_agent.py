import os
import sys

# Add parent directory to path to import base_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent

class SeoMetaOptimizerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="SEO Meta Copy Optimizer",
            system_instruction="You are an SEO expert. Your job is to analyze article outlines or website copy and generate optimized SEO page titles, meta descriptions, and heading structure suggestions."
        )

if __name__ == "__main__":
    agent = SeoMetaOptimizerAgent()
    print("="*50)
    print(f"Running {agent.name}...")
    print("="*50)
    user_prompt = input("Enter your request: ").strip()
    
    print("\nProcessing request...")
    response = agent.run(user_prompt)
    print("\n[Response]:")
    print(response)
