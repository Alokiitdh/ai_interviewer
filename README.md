Thanks! Based on your code, here is a complete and professional `README.md` you can use for your GitHub repo:

* * * * *

```

# 🤖 AI Interviewer (LangGraph-based)

AI Interviewer is a multi-agent interview simulation system powered by **LangGraph** and **LLMs (OpenAI or local models)**. It conducts technical interviews by:

- Asking topic-based theoretical questions

- Evaluating answers using a scoring rubric

- Summarizing the candidate's performance

---

## 📦 Features

- ✅ Multi-agent LangGraph: Question → Evaluation → Performance

- ✅ OpenAI or Local LLMs (e.g., via Groq, Ollama, etc.)

- ✅ CLI interface for live interview simulation

- ✅ Auto-scoring of answers based on technical depth, clarity, terminology, etc.

- ✅ Final score and performance summary after 5 rounds

- ✅ Optional Tavily search tool for grounded question generation

---

## 🛠️ Technologies Used

- [LangGraph](https://docs.langgraph.dev/)

- [LangChain](https://www.langchain.com/)

- [OpenAI API](https://platform.openai.com/) or [Groq API](https://console.groq.com/)

- [Tavily Search API](https://www.tavily.com/) *(optional)*

- [Pydantic](https://docs.pydantic.dev/) (for structured response validation)

- Python 3.10+

---

## 📁 Project Structure

```

.

├── main.py # CLI runner

├── graph.py # LangGraph setup with agents + supervisor

├── llm.py # LLM config (OpenAI or local)

├── tools.py # External tools like Tavily

├── schema.py # Pydantic response schemas

├── prompts.py # All custom agent prompts

└── .env # API keys

```

---

## 🧠 System Flow & Design

1\. **Supervisor Agent** orchestrates the interview session.

2\. **Question Agent** generates a theoretical question based on the given topic.

3\. User answers the question via CLI.

4\. **Evaluation Agent** scores the answer on a 10-point rubric and summarizes it.

5\. After 5 rounds, the **Performance Agent**:

   - Calculates a total score out of 100

   - Generates a concise technical performance summary (max 250 chars)

### 🧭 Branching Logic

- If score < 6 → Supervisor can ask simpler follow-up questions (optional future enhancement)

- If user enters "FINAL_EVAL" → Shortcut to trigger performance summary

- Evaluation results are stored in internal state (only final summary is shown)

---

## 🚀 Setup Instructions

### 1. Clone the repo

```bash

git clone https://github.com/your-username/ai-interviewer.git

cd ai-interviewer

```

### 2\. Install dependencies

```

pip install -r requirements.txt

```

> If you use local LLMs (e.g., Groq or Ollama), include the corresponding LangChain packages.

### 3\. Add API keys to `.env`

```

OPEN_AI_KEY=your_openai_key_here

GROQ_API_KEY=your_groq_key_here

TAVILY_API_KEY=your_tavily_key_here  # Optional

```

### 4\. Run the CLI

```

python main.py

```

🔧 Optional Features Implemented

--------------------------------

-   ✅ Dynamic prompt templates for each agent

-   ✅ LangGraph memory using `InMemoryStore` and `InMemorySaver`

-   ✅ Structured schema validation via Pydantic

-   ✅ Configurable LLM backend (`ChatOpenAI` / `ChatGroq`)

-   ✅ Plug-and-play external tools (e.g., Tavily)

📄 License

----------

MIT License --- free to use and modify.

* * * * *

🙌 Acknowledgements

-------------------

Built using:

-   [LangGraph](https://github.com/langchain-ai/langgraph)

-   [OpenAI](https://platform.openai.com/)

-   [LangChain](https://www.langchain.com/)

-   [Tavily](https://www.tavily.com/)

```

---

```
