import os
import sys
# Add parent directory to path to import base_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent

class CrontabBuilderAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Crontab Builder",
            system_instruction="You are a cron schedule helper agent. Convert human-readable time schedules into valid crontab syntax and explain when they trigger."
        )

if __name__ == "__main__":
    agent = CrontabBuilderAgent()
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
