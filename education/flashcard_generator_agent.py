import os
import sys

# Add parent directory to path to import base_agent
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from base_agent import BaseAgent

class FlashcardGeneratorAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Interactive Flashcard Generator",
            system_instruction="You are an educational assistant. Your job is to convert textbooks, notes, or research papers into interactive Q&A pairs and flashcard decks (such as Anki-compatible layouts)."
        )

if __name__ == "__main__":
    agent = FlashcardGeneratorAgent()
    print("="*50)
    print(f"Running {agent.name}...")
    print("="*50)
    user_prompt = input("Enter your request: ").strip()
    
    print("\nProcessing request...")
    response = agent.run(user_prompt)
    print("\n[Response]:")
    print(response)
