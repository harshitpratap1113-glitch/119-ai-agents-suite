import os
import sys

# Add parent directory to path to import base_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent

class ProjectIssueCreatorAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Support-to-Jira Project Agent",
            system_instruction="You are a project manager. Your job is to analyze customer complaints, chat transcripts, or support tickets, and convert them into clear, structured Jira/Linear bug reports and developer tasks."
        )

if __name__ == "__main__":
    agent = ProjectIssueCreatorAgent()
    print("="*50)
    print(f"Running {agent.name}...")
    print("="*50)
    user_prompt = input("Enter your request: ").strip()
    
    print("\nProcessing request...")
    response = agent.run(user_prompt)
    print("\n[Response]:")
    print(response)
