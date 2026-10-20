# 🤖 AI Agent Ecosystem: 119 Specialized AI Agents

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![AI Engine](https://img.shields.io/badge/Engine-Google%20Gemini%202.5%20Flash-orange.svg)](https://aistudio.google.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Zero Bloat](https://img.shields.io/badge/Framework-Zero--Bloat%20Pure%20Python-green.svg)](#architecture)

An open-source, modular collection of **119 specialized AI agents** organized across 7 core domains. Built for developers, creators, analysts, and operators who need fast, focused, zero-bloat AI assistants directly from their terminal or desktop.

---

## ⚡ Quickstart (Under 30 Seconds)

### 1. Clone & Install Dependencies
```bash
git clone https://github.com/harshitpratap1113-glitch/ai-agent-ecosystem.git
cd ai-agent-ecosystem
pip install -r requirements.txt
```

### 2. Configure Your API Key
Copy `.env.example` to `.env` and paste your free Gemini API key:
```bash
cp .env.example .env
```
*(Get a free Gemini API Key at [Google AI Studio](https://aistudio.google.com/app/apikey))*

### 3. Run Any Agent

#### Option A: Unified Master CLI
```bash
# List all 119 agents
python cli.py list

# Search agents by keyword
python cli.py search sql

# Run a specific agent
python cli.py run bug_finder "def add(a, b): return a - b"

# Interactive menu mode
python cli.py interactive
```

#### Option B: Direct Python Execution
```bash
python coding/bug_finder_agent.py "def divide(a, b): return a / b"
python writing/cold_email_agent.py "Pitching AI automation to e-commerce founders"
```

#### Option C: 1-Click Desktop Runners (Windows)
Double-click any `.bat` script inside the `runners/` directory (e.g., `runners/writing/run_cold_email.bat`) for an instant interactive window.

---

## 🏛️ Ecosystem Overview (7 Domains)

```
ai-agent-ecosystem/
├── base_agent.py          # Resilient multi-model execution engine
├── cli.py                 # Unified CLI master controller
├── requirements.txt       # Lightweight dependencies
│
├── coding/                # 16 Developer & Engineering Agents
├── writing/               # 17 Content, Copywriting & Media Agents
├── data/                  # 18 Data Engineering, SQL & Analytics Agents
├── productivity/          # 17 Business, PM & Career Agents
├── education/             # 17 Learning, Tutors & Academic Agents
├── lifestyle/             # 17 Fitness, Habits & Personal Agents
├── utilities/             # 17 System Diagnostics & Scripts Agents
└── runners/               # 119 Portable 1-Click Windows Runners
```

---

## 📋 Complete Agent Directory

### 💻 1. Coding & Development (16 Agents)
| Agent | File | Purpose |
| :--- | :--- | :--- |
| **Bug Finder** | `coding/bug_finder_agent.py` | Detects syntax bugs, logic flaws, and performance bottlenecks with fixes. |
| **Code Refactor** | `coding/code_refactor_agent.py` | Refactors code according to DRY and SOLID clean-code principles. |
| **Legacy Code Refactorer** | `coding/legacy_refactorer_agent.py` | Modernizes legacy codebases to current language standards. |
| **Unit Test Generator** | `coding/unit_test_agent.py` | Generates comprehensive test suites across pytest, jest, etc. |
| **SQL Optimizer** | `coding/sql_optimizer_agent.py` | Analyzes query plans, suggests indexes, and rewrites slow queries. |
| **Regex Generator** | `coding/regex_generator_agent.py` | Creates and explains regular expression patterns for text matching. |
| **Dockerfile Generator** | `coding/dockerfile_generator_agent.py` | Writes production-ready Dockerfile and docker-compose configurations. |
| **Crontab Builder** | `coding/crontab_builder_agent.py` | Translates human-readable schedules into valid crontab syntax. |
| **Git Commit Assistant** | `coding/git_commit_agent.py` | Writes conventional commit messages from git diffs. |
| **API Doc Generator** | `coding/api_doc_agent.py` | Converts route definitions into OpenAPI/Swagger and Markdown documentation. |
| **Docstring Generator** | `coding/docstring_generator_agent.py` | Generates standard Google/Sphinx style docstrings for functions and classes. |
| **Env Setup Guard** | `coding/env_setup_guard_agent.py` | Analyzes project dependencies to create step-by-step local setup guides. |
| **JSON Schema Builder** | `coding/json_schema_agent.py` | Converts JSON structures and models into valid JSON Schema specifications. |
| **CSS Grid & Flexbox** | `coding/css_grid_agent.py` | Creates responsive, modern CSS layouts from component descriptions. |
| **Markdown Converter** | `coding/markdown_converter_agent.py` | Converts HTML, XML, or JSON inputs into semantic Markdown documents. |
| **Bash & Shell Helper** | `coding/bash_helper_agent.py` | Generates safe, tested Bash and PowerShell automation commands. |

### ✍️ 2. Writing & Content Marketing (17 Agents)
| Agent | File | Purpose |
| :--- | :--- | :--- |
| **Cold Email Specialist** | `writing/cold_email_agent.py` | Writes personalized, high-converting B2B outreach emails. |
| **Cold Outreach Pitch** | `writing/cold_outreach_agent.py` | Crafts LinkedIn connection messages and conversion-focused sales pitches. |
| **Ad Copywriter** | `writing/copywriter_agent.py` | Writes persuasive copy using AIDA, PAS, and Before-After-Bridge frameworks. |
| **Headline & Hook** | `writing/headline_hook_agent.py` | Generates high-CTR video titles, headlines, and subject lines. |
| **SEO Optimizer** | `writing/seo_optimizer_agent.py` | Analyzes content and suggests keyword placement for search rankings. |
| **SEO Meta Optimizer** | `writing/seo_meta_optimizer_agent.py` | Generates optimized meta titles, descriptions, and OpenGraph tags. |
| **Blog Post Specialist** | `writing/blog_post_agent.py` | Outlines and drafts comprehensive, engaging long-form articles. |
| **Newsletter Writer** | `writing/newsletter_agent.py` | Drafts informative, high-retention weekly and monthly newsletters. |
| **Social Media Copy** | `writing/social_media_agent.py` | Formats platform-specific posts for X/Twitter, LinkedIn, and Instagram. |
| **Proofreader** | `writing/proofreader_agent.py` | Corrects grammar, punctuation, and flow with detailed explanations. |
| **Paraphraser** | `writing/paraphraser_agent.py` | Rewrites paragraphs to improve readability while maintaining original intent. |
| **FAQ Generator** | `writing/faq_generator_agent.py` | Generates comprehensive FAQ sections from product features. |
| **Press Release** | `writing/press_release_agent.py` | Formats media-ready press releases in standard AP journalistic style. |
| **Speech Writer** | `writing/speech_writer_agent.py` | Drafts keynote speeches, toasts, and presentation scripts. |
| **Story Generator** | `writing/story_generator_agent.py` | Brainstorms narrative arcs, character sketches, and fictional scenes. |
| **Screenplay Assistant** | `writing/screenplay_agent.py` | Formats screenplays with industry-standard sluglines, action, and dialogue. |
| **Poetry & Rhymes** | `writing/poetry_agent.py` | Composes sonnets, free verse, haikus, and rhymed verses on themes. |

### 📊 3. Data & Analytics (18 Agents)
| Agent | File | Purpose |
| :--- | :--- | :--- |
| **CSV Summarizer** | `data/csv_summarizer_agent.py` | Calculates statistics and extracts key trends from raw CSV datasets. |
| **Excel Formula Generator**| `data/excel_formula_agent.py` | Generates complex formulas (INDEX/MATCH, XLOOKUP, nested logic). |
| **Natural English to SQL** | `data/sql_query_generator_agent.py` | Converts plain-English data questions into executable SQL queries. |
| **SQL Code Formatter** | `data/sql_formatter_agent.py` | Formats messy queries into clean, beautifully indented SQL. |
| **Data Anomaly Detector** | `data/data_anomaly_detector_agent.py` | Identifies unusual spikes, data entry errors, and schema drift. |
| **Outlier Detector** | `data/outlier_detector_agent.py` | Flags mathematical and logical anomalies in tabular data. |
| **Data Anonymizer** | `data/data_anonymizer_agent.py` | Masks Personally Identifiable Information (PII) for compliance. |
| **Log Parser** | `data/log_parser_agent.py` | Extracts error frequencies, IP metrics, and stack trace summaries from logs. |
| **JSON Parser & Cleaner** | `data/json_parser_agent.py` | Validates, fixes malformed strings, and converts JSON to tables. |
| **XML to JSON Converter** | `data/xml_to_json_agent.py` | Transforms nested XML tags and attributes into valid JSON structures. |
| **PDF Analyzer** | `data/pdf_analyzer_agent.py` | Extracts structured key-value pairs and tabular data from raw PDF text. |
| **Regex Data Extractor** | `data/regex_extractor_agent.py` | Pulls emails, URLs, IP addresses, and dates from unstructured text dumps. |
| **Sentiment Analyzer** | `data/sentiment_analyzer_agent.py` | Classifies customer reviews and comments into Positive/Negative/Neutral. |
| **Chart Suggester** | `data/chart_suggester_agent.py` | Recommends optimal visualization types (scatter, heatmap, bar) for datasets. |
| **Trend Spotter** | `data/trend_spotter_agent.py` | Evaluates market and technology news to identify emerging macro trends. |
| **Web Scraper Helper** | `data/web_scraper_helper_agent.py` | Writes BeautifulSoup, CSS, and XPath selectors for web scraping. |
| **Currency Converter** | `data/currency_converter_agent.py` | Analyzes forex rates and computes cross-currency conversions. |
| **Metric Unit Converter** | `data/metric_converter_agent.py` | Converts measurements across metric and imperial systems accurately. |

### ⚡ 4. Productivity & Business Strategy (17 Agents)
| Agent | File | Purpose |
| :--- | :--- | :--- |
| **Project Breakdown** | `productivity/project_breakdown_agent.py` | Deconstructs large roadmaps into phases, milestones, and task checklists. |
| **Support to Jira Issue** | `productivity/project_issue_creator_agent.py` | Converts user complaints and chat transcripts into structured bug tickets. |
| **Pitch Deck Strategist** | `productivity/pitch_deck_agent.py` | Outlines slide-by-slide investor presentations (Problem, Solution, TAM). |
| **SWOT Analyst** | `productivity/swot_analyst_agent.py` | Generates 4-quadrant Strengths, Weaknesses, Opportunities & Threats reports. |
| **Market Researcher** | `productivity/market_researcher_agent.py` | Designs market survey questions, customer personas, and research plans. |
| **Meeting Summarizer** | `productivity/meeting_summarizer_agent.py` | Distills raw meeting notes into action items, owners, and decisions. |
| **Calendar Time Blocker** | `productivity/calendar_time_blocker_agent.py` | Allocates focused hourly blocks for task lists to eliminate overwhelm. |
| **Goal Tracker (OKR)** | `productivity/goal_tracker_agent.py` | Converts goals into measurable Objectives and Key Results (OKRs). |
| **Expense & Budget** | `productivity/expense_tracker_agent.py` | Categorizes spend items and suggests target saving strategies. |
| **Invoice Generator** | `productivity/invoice_generator_agent.py` | Generates clean Markdown billing tables and itemized invoice templates. |
| **Resume & CV Reviewer** | `productivity/resume_reviewer_agent.py` | Audits CVs against target job descriptions and rewrites weak bullets. |
| **Cover Letter Builder** | `productivity/cover_letter_agent.py` | Tailors personalized cover letters matching candidate experience to roles. |
| **Interview Prep Coach** | `productivity/interview_prep_agent.py` | Generates role-specific behavioral (STAR) and technical interview drills. |
| **Job Description Writer**| `productivity/job_description_agent.py` | Writes inclusive, clear job specs with responsibilities and benefits. |
| **Decision Helper** | `productivity/decision_helper_agent.py` | Builds weighted trade-off matrices to evaluate high-stakes choices. |
| **Time Management Coach**| `productivity/time_management_agent.py` | Recommends productivity systems (Pomodoro, Time Blocking, Eisenhower). |
| **Travel Business Planner**| `productivity/travel_planner_agent.py` | Plans seamless day-by-day travel itineraries based on schedules and budget. |

### 🎓 5. Education & Tutoring (17 Agents)
| Agent | File | Purpose |
| :--- | :--- | :--- |
| **Coding Tutor** | `education/coding_tutor_agent.py` | Explains data structures and algorithms using practical analogies. |
| **Math Tutor** | `education/math_tutor_agent.py` | Provides step-by-step solutions for algebra, calculus, and arithmetic. |
| **Science Tutor** | `education/science_tutor_agent.py` | Explains physics, chemistry, and biology principles clearly. |
| **Concept Explainer (ELI5)**| `education/concept_explainer_agent.py` | Simplifies complex theoretical concepts using beginner-friendly language. |
| **Book Summarizer** | `education/book_summarizer_agent.py` | Distills non-fiction books into key takeaways and core frameworks. |
| **Study Planner** | `education/study_planner_agent.py` | Constructs revision schedules leading up to examinations. |
| **Syllabus Gap Finder** | `education/syllabus_gap_finder_agent.py` | Compares student preparation against curriculum requirements. |
| **Interactive Flashcards** | `education/flashcard_generator_agent.py` | Converts lecture notes into Anki-ready Q&A card decks. |
| **Flashcard Creator** | `education/flashcard_creator_agent.py` | Creates quick revision cards for spaced repetition study. |
| **Quiz Generator** | `education/quiz_generator_agent.py` | Creates multiple-choice and short-answer test papers with answer keys. |
| **Essay Planner** | `education/essay_planner_agent.py` | Outlines academic papers with thesis statements and transition flows. |
| **Bibliography Formatter** | `education/bibliography_formatter_agent.py` | Formats citations in APA, MLA, Chicago, and Harvard styles. |
| **Mnemonic Generator** | `education/mnemonic_generator_agent.py` | Creates acronyms and memory pegs to remember lists and sequences. |
| **Language Translator** | `education/language_translator_agent.py` | Translates idioms and nuanced text while preserving tone and context. |
| **Vocabulary Builder** | `education/vocabulary_builder_agent.py` | Provides definitions, etymology, synonyms, and usage examples. |
| **Synonym Finder** | `education/synonym_finder_agent.py` | Recommends elevated vocabulary alternatives to improve prose. |
| **History Fact Checker** | `education/history_fact_agent.py` | Cross-verifies historical events, timelines, and primary sources. |

### 🌿 6. Lifestyle & Personal Optimization (17 Agents)
| Agent | File | Purpose |
| :--- | :--- | :--- |
| **Meal Prep Planner** | `lifestyle/meal_prep_planner_agent.py` | Generates weekly meal prep plans and organized grocery shopping lists. |
| **Recipe Generator** | `lifestyle/recipe_generator_agent.py` | Formulates recipes based strictly on available ingredients and dietary needs. |
| **Workout Planner** | `lifestyle/workout_planner_agent.py` | Creates tailored strength and cardio routines for gym or home setups. |
| **Habit Tracker Coach** | `lifestyle/habit_tracker_agent.py` | Applies behavioral psychology to help establish routines and break habits. |
| **Digital Declutter** | `lifestyle/digital_declutter_agent.py` | Suggests folder structures and file pruning rules to free disk space. |
| **Daily Affirmation** | `lifestyle/daily_affirmation_agent.py` | Delivers focused mental clarity prompts and daily affirmations. |
| **Dream Interpreter** | `lifestyle/dream_interpreter_agent.py` | Explores symbolic and archetypal dream meanings. |
| **Gardening Coach** | `lifestyle/gardening_coach_agent.py` | Advises on watering schedules, pest diagnosis, and soil requirements. |
| **Interior Designer** | `lifestyle/interior_design_agent.py` | Suggests color palettes, furniture layouts, and lighting schemes. |
| **Gift Suggester** | `lifestyle/gift_suggester_agent.py` | Recommends curated gift ideas tailored to recipient interests and budget. |
| **Pet Care Advisor** | `lifestyle/pet_care_agent.py` | Outlines training steps, feeding guidelines, and care tips for common pets. |
| **Movie Recommender** | `lifestyle/movie_recommender_agent.py` | Suggests films and television series based on mood, genre, and past favorites. |
| **Book Recommender** | `lifestyle/book_recommender_agent.py` | Recommends fiction and non-fiction titles tailored to reading goals. |
| **Joke Teller** | `lifestyle/joke_teller_agent.py` | Generates puns, one-liners, and clean situational comedy. |
| **Riddle Master** | `lifestyle/riddle_generator_agent.py` | Writes logic puzzles and riddles with hidden reveal answers. |
| **Trivia Master** | `lifestyle/trivia_master_agent.py` | Runs multi-round themed trivia contests with scored answers. |
| **Text Adventure Master** | `lifestyle/adventure_game_agent.py` | Directs interactive choose-your-own-path role-playing stories. |

### 🛠️ 7. System Utilities & Diagnostics (17 Agents)
| Agent | File | Purpose |
| :--- | :--- | :--- |
| **System Health Monitor** | `utilities/system_health_agent.py` | Writes scripts to monitor CPU, memory, and disk utilization metrics. |
| **Directory Analyzer** | `utilities/directory_analyzer_agent.py` | Identifies oversized directories and disk-hogging files. |
| **File Organizer** | `utilities/file_organizer_agent.py` | Generates scripts to automatically sort messy download directories by type. |
| **Duplicate File Finder** | `utilities/duplicate_finder_agent.py` | Detects duplicate files using cryptographic hash comparisons. |
| **Env Inspector** | `utilities/env_inspector_agent.py` | Verifies environment variables and prevents accidental secret exposure. |
| **Backup Scheduler** | `utilities/backup_scheduler_agent.py` | Designs automated 3-2-1 backup rotation strategies and scripts. |
| **Password Generator** | `utilities/password_generator_agent.py` | Generates high-entropy passwords with configurable character sets. |
| **Hash Generator** | `utilities/hash_generator_agent.py` | Computes MD5, SHA-1, and SHA-256 hashes for strings and files. |
| **Base64 Encoder** | `utilities/base64_encoder_agent.py` | Encodes and decodes Base64 strings and binary payloads. |
| **UUID Generator** | `utilities/uuid_generator_agent.py` | Generates standard UUIDv4 identifiers. |
| **Port Scanner Advisor** | `utilities/port_scanner_agent.py` | Explains socket scanning and generates network diagnostic scripts. |
| **IP & Subnet Lookup** | `utilities/ip_lookup_agent.py` | Explains CIDR subnetting, IP classifications, and geolocation queries. |
| **Subscription Tracker** | `utilities/subscription_tracker_agent.py` | Audits recurring software subscriptions and trial expiration dates. |
| **Timestamp Converter** | `utilities/timestamp_converter_agent.py` | Converts Unix epoch timestamps to human-readable UTC/local times. |
| **Markdown Table** | `utilities/markdown_table_agent.py` | Converts raw CSV and tab-delimited text into aligned Markdown tables. |
| **URL Shortener** | `utilities/url_shortener_agent.py` | Outlines database schemas and base62 encoding for URL shorteners. |
| **Vacation Itinerary** | `utilities/travel_itinerary_agent.py` | Plans full vacation itineraries including flights, hotels, and attractions. |

---

## 🛠️ How to Create a New Agent (In 5 Lines)

Every agent inherits from `BaseAgent`. To create agent #120:

```python
from base_agent import BaseAgent

class KubernetesAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="Kubernetes Architect",
            system_instruction="You are an expert Kubernetes architect. Generate clean, production-grade K8s YAML manifests."
        )

if __name__ == "__main__":
    agent = KubernetesAgent()
    print(agent.run("Create a deployment with 3 replicas for an Nginx reverse proxy."))
```

---

## 🔒 Security & Privacy

* **100% Local Execution:** Code runs directly on your machine.
* **No Intermediary Proxies:** API calls travel directly from your client to the AI provider endpoint.
* **Zero Secret Leakage:** `.env` is strictly ignored via `.gitignore`. Never commit keys.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
