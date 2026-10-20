import os
import sys
import time

class BaseAgent:
    """
    BaseAgent: Advanced, resilient core execution engine for the AI Agent Ecosystem.
    Supports Google Gemini (Native SDK & GenerativeAI fallback), OpenRouter, OpenAI, and Anthropic.
    """
    def __init__(self, name, system_instruction, tools=None):
        self.name = name
        self.system_instruction = system_instruction
        self.tools = tools or []
        self.provider = None
        self.client = None
        self.model_name = None
        
        # Load API keys from .env or environment
        api_keys = self._load_env_keys()
        
        # 1. Native Google Gemini (Recommended)
        if api_keys.get("GEMINI_API_KEY") and not api_keys["GEMINI_API_KEY"].startswith("sk-or-"):
            gemini_key = api_keys["GEMINI_API_KEY"]
            # Try new google-genai SDK first
            try:
                from google import genai
                self.client = genai.Client(api_key=gemini_key)
                self.provider = "gemini"
                self.model_name = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
            except ImportError:
                # Fallback to legacy google-generativeai SDK
                try:
                    import google.generativeai as legacy_genai
                    legacy_genai.configure(api_key=gemini_key)
                    self.client = legacy_genai.GenerativeModel(
                        model_name=os.environ.get("GEMINI_MODEL", "gemini-1.5-flash"),
                        system_instruction=self.system_instruction
                    )
                    self.provider = "gemini_legacy"
                    self.model_name = os.environ.get("GEMINI_MODEL", "gemini-1.5-flash")
                except ImportError:
                    print("[Warning] Neither 'google-genai' nor 'google-generativeai' installed.")
                    print("Run: pip install google-genai")

        # 2. OpenRouter Fallback
        elif api_keys.get("OPENROUTER_API_KEY") or (api_keys.get("GEMINI_API_KEY") and api_keys["GEMINI_API_KEY"].startswith("sk-or-")) or (api_keys.get("OPENAI_API_KEY") and api_keys["OPENAI_API_KEY"].startswith("sk-or-")):
            key = api_keys.get("OPENROUTER_API_KEY") or api_keys.get("GEMINI_API_KEY") or api_keys.get("OPENAI_API_KEY")
            try:
                import openai
                self.client = openai.OpenAI(
                    base_url="https://openrouter.ai/api/v1",
                    api_key=key
                )
                self.provider = "openrouter"
                self.model_name = os.environ.get("OPENROUTER_MODEL", "google/gemini-2.5-flash")
            except ImportError:
                print("[Warning] 'openai' library not installed for OpenRouter. Run: pip install openai")

        # 3. OpenAI Direct
        elif api_keys.get("OPENAI_API_KEY"):
            try:
                import openai
                self.client = openai.OpenAI(api_key=api_keys["OPENAI_API_KEY"])
                self.provider = "openai"
                self.model_name = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
            except ImportError:
                print("[Warning] 'openai' library not installed. Run: pip install openai")

        # 4. Anthropic Claude Direct
        elif api_keys.get("ANTHROPIC_API_KEY"):
            try:
                import anthropic
                self.client = anthropic.Anthropic(api_key=api_keys["ANTHROPIC_API_KEY"])
                self.provider = "anthropic"
                self.model_name = os.environ.get("ANTHROPIC_MODEL", "claude-3-5-haiku-20241022")
            except ImportError:
                print("[Warning] 'anthropic' library not installed. Run: pip install anthropic")

    def _load_env_keys(self):
        keys = {
            "GEMINI_API_KEY": None,
            "OPENAI_API_KEY": None,
            "ANTHROPIC_API_KEY": None,
            "OPENROUTER_API_KEY": None
        }
        # Check potential .env locations: current working directory & script's base directory
        base_dir = os.path.dirname(os.path.abspath(__file__))
        candidate_paths = [
            os.path.join(base_dir, ".env"),
            os.path.join(os.getcwd(), ".env")
        ]
        
        for env_path in candidate_paths:
            if os.path.exists(env_path):
                try:
                    with open(env_path, "r", encoding="utf-8") as f:
                        for line in f:
                            line = line.strip()
                            if line and not line.startswith("#") and "=" in line:
                                k, v = line.split("=", 1)
                                k = k.strip()
                                v = v.strip().strip('"').strip("'")
                                if k in keys and not keys[k]:
                                    keys[k] = v
                except Exception:
                    pass

        # Environment variable fallback
        for k in keys:
            if not keys[k]:
                keys[k] = os.environ.get(k)
                    
        return keys

    def run(self, prompt, max_tokens=None):
        if not self.client:
            return (
                f"\n[!] Configuration Notice for {self.name}:\n"
                f"No active AI client could be initialized. Please set your API key:\n"
                f"  1. Copy .env.example to .env\n"
                f"  2. Add your GEMINI_API_KEY=your_key_here\n"
                f"  3. Get a free key at: https://aistudio.google.com/app/apikey\n"
                f"  4. Install library: pip install google-genai\n"
            )

        print(f"[{self.name}] Querying {self.provider} ({self.model_name})...")
        start_time = time.time()
        
        try:
            # 1. Native Google GenAI
            if self.provider == "gemini":
                from google.genai import types
                config_args = {"system_instruction": self.system_instruction}
                if max_tokens:
                    config_args["max_output_tokens"] = max_tokens
                
                # Resilient fallback across flash models
                candidate_models = [self.model_name, "gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash"]
                last_err = None
                for m in candidate_models:
                    try:
                        response = self.client.models.generate_content(
                            model=m,
                            contents=prompt,
                            config=types.GenerateContentConfig(**config_args)
                        )
                        elapsed = time.time() - start_time
                        return f"{response.text}\n\n*(Generated in {elapsed:.2f}s via {m})*"
                    except Exception as err:
                        last_err = err
                        continue
                raise last_err

            # 2. Legacy Google GenerativeAI
            elif self.provider == "gemini_legacy":
                response = self.client.generate_content(prompt)
                elapsed = time.time() - start_time
                return f"{response.text}\n\n*(Generated in {elapsed:.2f}s via legacy {self.model_name})*"

            # 3. OpenAI
            elif self.provider == "openai":
                kwargs = {
                    "model": self.model_name,
                    "messages": [
                        {"role": "system", "content": self.system_instruction},
                        {"role": "user", "content": prompt}
                    ]
                }
                if max_tokens:
                    kwargs["max_tokens"] = max_tokens
                response = self.client.chat.completions.create(**kwargs)
                elapsed = time.time() - start_time
                return f"{response.choices[0].message.content}\n\n*(Generated in {elapsed:.2f}s via {self.model_name})*"

            # 4. OpenRouter
            elif self.provider == "openrouter":
                limit = max_tokens if max_tokens else 1000
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    max_tokens=limit,
                    messages=[
                        {"role": "system", "content": self.system_instruction},
                        {"role": "user", "content": prompt}
                    ]
                )
                elapsed = time.time() - start_time
                return f"{response.choices[0].message.content}\n\n*(Generated in {elapsed:.2f}s via OpenRouter)*"

            # 5. Anthropic Claude
            elif self.provider == "anthropic":
                response = self.client.messages.create(
                    model=self.model_name,
                    max_tokens=max_tokens or 2048,
                    system=self.system_instruction,
                    messages=[{"role": "user", "content": prompt}]
                )
                elapsed = time.time() - start_time
                return f"{response.content[0].text}\n\n*(Generated in {elapsed:.2f}s via {self.model_name})*"

        except Exception as e:
            return f"\n[!] Error running {self.name} via {self.provider}:\n{str(e)}"
