#!/usr/bin/env python3
"""
AI Agent Ecosystem - Master CLI Controller
Execute, search, and manage all 119 specialized AI agents from a single unified interface.
"""

import os
import sys
import importlib.util

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CATEGORIES = ['coding', 'writing', 'data', 'productivity', 'education', 'lifestyle', 'utilities']

def get_all_agents():
    agents = []
    for cat in CATEGORIES:
        cat_dir = os.path.join(ROOT_DIR, cat)
        if os.path.exists(cat_dir):
            for f in sorted(os.listdir(cat_dir)):
                if f.endswith('_agent.py'):
                    name = f.replace('_agent.py', '')
                    agents.append({
                        'category': cat,
                        'filename': f,
                        'name': name,
                        'path': os.path.join(cat_dir, f)
                    })
    return agents

def load_agent(agent_info):
    spec = importlib.util.spec_from_file_location(agent_info['name'], agent_info['path'])
    module = importlib.util.module_from_spec(spec)
    sys.modules[agent_info['name']] = module
    spec.loader.exec_module(module)
    
    # Locate Agent class
    for attr in dir(module):
        if attr.endswith('Agent') and attr != 'BaseAgent':
            agent_class = getattr(module, attr)
            return agent_class()
    return None

def print_banner():
    print("""
==================================================================
           AI AGENT ECOSYSTEM (119 SPECIALIZED AGENTS)           
==================================================================
""")

def cmd_list():
    agents = get_all_agents()
    print_banner()
    print(f"Total Agents Installed: {len(agents)}\n")
    current_cat = None
    for a in agents:
        if a['category'] != current_cat:
            current_cat = a['category']
            print(f"\n--- [{current_cat.upper()}] ---")
        print(f"  * {a['name']:<30} (python {a['category']}/{a['filename']})")
    print("\nRun any agent via: python cli.py run <agent_name> [prompt]")

def cmd_search(keyword):
    agents = get_all_agents()
    matches = [a for a in agents if keyword.lower() in a['name'].lower() or keyword.lower() in a['category'].lower()]
    print_banner()
    print(f"Search results for '{keyword}' ({len(matches)} matches found):\n")
    for a in matches:
        print(f"  * [{a['category'].upper()}] {a['name']:<25} -> python cli.py run {a['name']}")

def cmd_run(target_name, prompt=None):
    agents = get_all_agents()
    matched = next((a for a in agents if a['name'].lower() == target_name.lower().replace('-', '_')), None)
    
    if not matched:
        # Partial match fallback
        candidates = [a for a in agents if target_name.lower() in a['name'].lower()]
        if len(candidates) == 1:
            matched = candidates[0]
        elif len(candidates) > 1:
            print(f"[!] Multiple agents match '{target_name}':")
            for c in candidates:
                print(f"  - {c['name']}")
            return
        else:
            print(f"[!] Agent '{target_name}' not found. Run 'python cli.py list' to see all 119 agents.")
            return

    agent_inst = load_agent(matched)
    if not agent_inst:
        print(f"[!] Failed to instantiate agent: {matched['name']}")
        return

    print_banner()
    print(f"Active Agent: {agent_inst.name} ({matched['category'].upper()})")
    
    if not prompt:
        prompt = input(f"\nEnter prompt for {agent_inst.name}: ").strip()
    
    if not prompt:
        print("[!] No prompt provided. Exiting.")
        return

    print("\n" + "="*50)
    print("Running...")
    print("="*50)
    response = agent_inst.run(prompt)
    print("\n[Response]:\n")
    print(response)

def cmd_interactive():
    print_banner()
    agents = get_all_agents()
    print("Select a Category:")
    for idx, cat in enumerate(CATEGORIES, 1):
        count = len([a for a in agents if a['category'] == cat])
        print(f"  [{idx}] {cat.capitalize()} ({count} agents)")
    
    try:
        cat_choice = int(input("\nEnter category number: ").strip())
        selected_cat = CATEGORIES[cat_choice - 1]
    except Exception:
        print("[!] Invalid category selection.")
        return

    cat_agents = [a for a in agents if a['category'] == selected_cat]
    print(f"\nSelect an Agent from [{selected_cat.upper()}]:")
    for idx, a in enumerate(cat_agents, 1):
        print(f"  [{idx}] {a['name']}")

    try:
        agent_choice = int(input("\nEnter agent number: ").strip())
        selected_agent = cat_agents[agent_choice - 1]
    except Exception:
        print("[!] Invalid agent selection.")
        return

    cmd_run(selected_agent['name'])

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help']:
        print_banner()
        print("""Usage:
  python cli.py list                  List all 119 agents grouped by category
  python cli.py search <keyword>      Search agents by topic (e.g., 'sql', 'email')
  python cli.py run <agent> [prompt]  Run a specific agent
  python cli.py interactive          Interactive menu mode
""")
        return

    cmd = sys.argv[1].lower()
    if cmd == 'list':
        cmd_list()
    elif cmd == 'search':
        if len(sys.argv) < 3:
            print("Please specify a search keyword: python cli.py search <keyword>")
        else:
            cmd_search(sys.argv[2])
    elif cmd == 'run':
        if len(sys.argv) < 3:
            print("Please specify an agent: python cli.py run <agent_name> [prompt]")
        else:
            prompt = " ".join(sys.argv[3:]) if len(sys.argv) > 3 else None
            cmd_run(sys.argv[2], prompt)
    elif cmd in ['interactive', 'menu']:
        cmd_interactive()
    else:
        # Direct agent shortcut: python cli.py bug_finder "prompt"
        prompt = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else None
        cmd_run(cmd, prompt)

if __name__ == '__main__':
    main()
