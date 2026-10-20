import os
import sys
import re

# Force UTF-8 encoding on standard I/O streams to prevent Windows CMD charmap crashes with emojis
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
        sys.stdin.reconfigure(encoding='utf-8')
    except:
        pass
import json
import importlib.util
import inspect

# Add current folder to path to import base_agent
agents_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(agents_dir)
from base_agent import BaseAgent

class MasterAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Master Coordinator Agent",
            system_instruction="""You are the Master Coordinator of a team of 120+ specialized AI agents. Your job is to analyze the user's request, decide which agent(s) are needed to solve it, and plan their execution.

You can delegate the task to a single agent or create a multi-agent team/pipeline where agents work sequentially, passing outputs from one to the next.

Respond ONLY with a JSON array of steps. Each step must specify:
1. "agent_key": The unique identifier of the agent (e.g. "coding/bug_finder_agent.py").
2. "prompt": The specific instruction for this agent. If this agent needs the output of a previous agent, use the placeholder [PREVIOUS_OUTPUT] in the prompt.

Example output:
[
  {"agent_key": "coding/bug_finder_agent.py", "prompt": "Find bugs in this code: ..."},
  {"agent_key": "coding/code_refactor_agent.py", "prompt": "Refactor the code based on these bugs: [PREVIOUS_OUTPUT]"}
]
"""
        )
        self.registry = {}
        self.load_agents()

    def load_agents(self):
        print("Registering available agents dynamically...")
        categories = ["coding", "writing", "data", "productivity", "education", "lifestyle", "utilities"]
        
        for cat in categories:
            cat_dir = os.path.join(agents_dir, cat)
            if not os.path.exists(cat_dir):
                continue
            
            for file in os.listdir(cat_dir):
                if file.endswith("_agent.py"):
                    file_path = os.path.join(cat_dir, file)
                    agent_key = f"{cat}/{file}"
                    
                    try:
                        # Dynamically import the module
                        module_name = file.replace(".py", "")
                        spec = importlib.util.spec_from_file_location(module_name, file_path)
                        module = importlib.util.module_from_spec(spec)
                        # Temporarily add category path to sys.path to allow base_agent imports inside agents
                        sys.path.append(cat_dir)
                        spec.loader.exec_module(module)
                        sys.path.remove(cat_dir)
                        
                        # Find the class that inherits from BaseAgent
                        for name, obj in inspect.getmembers(module, inspect.isclass):
                            if issubclass(obj, BaseAgent) and obj != BaseAgent and obj != MasterAgent:
                                # Instantiate agent to read attributes
                                instance = obj()
                                self.registry[agent_key] = {
                                    "class_obj": obj,
                                    "name": instance.name,
                                    "system_instruction": instance.system_instruction,
                                    "file_path": file_path
                                }
                                break
                    except Exception as e:
                        # Fallback to simple regex parsing if import fails
                        try:
                            with open(file_path, "r", encoding="utf-8") as f:
                                content = f.read()
                            name_match = re.search(r'name\s*=\s*["\'](.*?)["\']', content)
                            inst_match = re.search(r'system_instruction\s*=\s*["\']{3}(.*?)["\']{3}|system_instruction\s*=\s*["\'](.*?)["\']', content, re.DOTALL)
                            
                            name = name_match.group(1) if name_match else file.replace("_agent.py", "").replace("_", " ").title()
                            instruction = ""
                            if inst_match:
                                instruction = inst_match.group(1) if inst_match.group(1) else inst_match.group(2)
                            
                            self.registry[agent_key] = {
                                "class_obj": None,
                                "name": name,
                                "system_instruction": instruction,
                                "file_path": file_path
                            }
                        except:
                            pass

        print(f"Registered {len(self.registry)} agents successfully!\n")

    def execute_pipeline(self, task):
        # 1. Ask the Master LLM to design the delegation plan
        agents_list = ""
        for key, info in self.registry.items():
            agents_list += f"- Key: '{key}' | Name: '{info['name']}'\n"
            
        planning_prompt = f"""
Available Agents:
{agents_list}

User Task:
"{task}"

Analyze the task and determine which agent(s) should execute it. 
Respond with a JSON plan of steps. Ensure the response contains ONLY the valid JSON array (no markdown code blocks, just raw JSON).
"""
        print("[Master Agent] Analyzing request and creating team delegation plan...")
        limit = 150 if self.provider == "openrouter" else 2048
        plan_response = self.run(planning_prompt, max_tokens=limit)
        
        # Clean markdown code block wraps if present
        plan_response = re.sub(r'```json\s*|\s*```', '', plan_response).strip()
        
        try:
            plan = json.loads(plan_response)
        except Exception as e:
            print(f"Error: Failed to parse execution plan JSON. Response was:\n{plan_response}")
            return "Could not create a structured delegation plan."
        
        print("\n" + "="*50)
        print("DELEGATION PLAN:")
        print("="*50)
        for i, step in enumerate(plan, 1):
            agent_name = self.registry.get(step["agent_key"], {}).get("name", step["agent_key"])
            print(f"Step {i}: Run '{agent_name}' ({step['agent_key']})")
            print(f"        Prompt: {step['prompt']}")
        print("="*50 + "\n")
        
        previous_output = ""
        
        # 2. Run each step in the plan sequentially
        for i, step in enumerate(plan, 1):
            agent_key = step["agent_key"]
            prompt = step["prompt"]
            
            if agent_key not in self.registry:
                # Self-healing: Check if the filename exists under a different category folder
                filename = os.path.basename(agent_key)
                corrected_key = None
                for reg_key in self.registry:
                    if os.path.basename(reg_key) == filename or reg_key.endswith(filename):
                        corrected_key = reg_key
                        break
                
                if corrected_key:
                    print(f"[Master Agent] Corrected folder routing for '{agent_key}' to '{corrected_key}'")
                    agent_key = corrected_key
                else:
                    print(f"Error: Agent '{agent_key}' not found in registry. Skipping step.")
                    continue
            
            # Replace placeholder with previous output
            if "[PREVIOUS_OUTPUT]" in prompt:
                prompt = prompt.replace("[PREVIOUS_OUTPUT]", previous_output)
                
            agent_info = self.registry[agent_key]
            print(f"\n[Executing Step {i}] Running {agent_info['name']}...")
            
            try:
                # Instantiate and run
                if agent_info["class_obj"]:
                    agent_instance = agent_info["class_obj"]()
                    step_output = agent_instance.run(prompt)
                else:
                    # Fallback to loading dynamically if class_obj was None
                    module_name = os.path.basename(agent_info["file_path"]).replace(".py", "")
                    spec = importlib.util.spec_from_file_location(module_name, agent_info["file_path"])
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    for name, obj in inspect.getmembers(module, inspect.isclass):
                        if issubclass(obj, BaseAgent) and obj != BaseAgent:
                            agent_instance = obj()
                            break
                    step_output = agent_instance.run(prompt)
                
                print(f"[Result from {agent_info['name']}]:\n{step_output}\n")
                previous_output = step_output
            except Exception as e:
                print(f"Error executing agent {agent_info['name']}: {e}")
                return f"Execution failed at step {i} ({agent_info['name']})."
                
        return previous_output

if __name__ == "__main__":
    master = MasterAgent()
    print("="*50)
    print("      MASTER COORDINATOR AGENT ACTIVATED")
    print("="*50)
    
    while True:
        print("\nDescribe your task (can be complex, requiring multiple agents):")
        print("Type 'exit' to quit.")
        task = input("\nYou: ").strip()
        
        if not task:
            continue
        if task.lower() in ['exit', 'quit']:
            print("Exiting Master Coordinator. Goodbye!")
            break
            
        final_result = master.execute_pipeline(task)
        print("\n" + "="*50)
        print("FINAL CONSOLIDATED RESULT:")
        print("="*50)
        print(final_result)
        print("="*50)

