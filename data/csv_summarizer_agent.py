import os
import sys
# Add parent directory to path to import base_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent

class CSVSummarizerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="C S V  Summarizer",
            system_instruction="You are a CSV data summarizer agent. Read raw CSV data, calculate basic statistics, and write structured markdown summaries of key insights."
        )

if __name__ == "__main__":
    agent = CSVSummarizerAgent()
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
