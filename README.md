# Automated Research Team (Agentic AI)

An **Agentic AI-powered research automation system** built using **CrewAI**, **Groq LLMs**, and **DuckDuckGo Search**. This project demonstrates how multiple AI agents can collaborate to research a topic, identify trends, and generate structured content automatically.

---

## 🚀 Project Overview

The Automated Research Team simulates a real-world research workflow using multiple specialized AI agents:

* **Research Analyst Agent** – Searches the web and identifies key trends
* **Content Strategist Agent** – Converts research insights into a professional blog-style report

The agents work **sequentially**, sharing context and outputs to produce a final consolidated report.

---

## 🧠 Key Features

* Agent-based architecture using **CrewAI**
* Uses **Groq-hosted LLaMA models** for fast inference
* Real-time web research via **DuckDuckGo Search**
* Environment-variable–based secret management (no hardcoded keys)
* Modular and extensible design (easy to add more agents or tools)

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **CrewAI** – Multi-agent orchestration
* **Groq LLM API** – Large Language Model inference
* **DuckDuckGo Search (ddgs)** – Free web search tool
* **python-dotenv** – Environment variable management

---

## 📂 Project Structure

```
Automated_Research_Team/
│
├── main.py          # Core application (agents, tasks, crew execution)
├── .gitignore       # Git ignore rules (env, venv, cache, etc.)
├── README.md        # Project documentation
└── .env             # Environment variables (NOT committed)
```

---

## 🔐 Environment Setup

### 1️⃣ Create a virtual environment

```bash
python -m venv venv
```

Activate it:

* **Windows**

```bash
venv\Scripts\activate
```

* **macOS / Linux**

```bash
source venv/bin/activate
```

---

### 2️⃣ Install dependencies

```bash
pip install crewai langchain-community langchain-groq ddgs python-dotenv
```

---

### 3️⃣ Configure environment variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

⚠️ **Never commit your `.env` file or API keys**

---

## ▶️ How to Run

```bash
python main.py
```

Example topic (inside `main.py`):

```python
topic = "Agentic AI trends 2025"
```

The output will include:

* Agent execution logs
* Identified trends
* A final markdown-formatted report

---

## 📌 Example Use Cases

* Market & technology trend analysis
* Automated research assistants
* Content ideation for blogs or reports
* Learning agentic AI workflows

---

## 🧩 Future Improvements

* Add citation tracking for sources
* Store research results in a database
* Add PDF / Markdown export
* Introduce parallel agent execution
* Add UI (Streamlit / FastAPI)

---

## 👤 Author

**Anirudha Kolay**
Computer Science & AI/ML Engineer
Tech & Data Enthusiast

---

## ⭐ If you find this useful

Give the repo a ⭐ and feel free to fork or contribute!
