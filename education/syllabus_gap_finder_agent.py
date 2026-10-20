import os
import sys

# Add parent directory to path to import base_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent

class SyllabusGapFinderAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Curriculum Syllabus Gap Finder",
            system_instruction="You are a study planner. Your job is to compare a student's list of completed topics against a target exam syllabus or curriculum and generate a customized study path to cover the gaps."
        )

if __name__ == "__main__":
    agent = SyllabusGapFinderAgent()
    print("="*50)
    print(f"Running {agent.name}...")
    print("="*50)
    user_prompt = input("Enter your request: ").strip()
    
    print("\nProcessing request...")
    response = agent.run(user_prompt)
    print("\n[Response]:")
    print(response)
