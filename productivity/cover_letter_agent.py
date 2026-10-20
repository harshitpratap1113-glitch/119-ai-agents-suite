import os
import sys
# Add parent directory to path to import base_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent

class CoverLetterAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Cover Letter",
            system_instruction="You are a cover letter builder. Write customized cover letters matching user experiences to job descriptions."
        )

if __name__ == "__main__":
    agent = CoverLetterAgent()
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
