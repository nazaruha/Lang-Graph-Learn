# 🦜🔗 LangChain & LangGraph Learning Lab

A repository dedicated to my journey exploring the LangChain ecosystem and building agentic AI architectures.

### 📌 Core Focus Areas:

- **LangChain:** Core abstractions, chains, prompt templates, and integrations.
- **LangGraph:** Stateful multi-agent systems, cyclical graphs, human-in-the-loop workflows, and tool calling.
- **LangSmith:** Agent evaluation, tracing, debugging, and performance monitoring.
- **Ecosystem & Tooling:** Vector stores, embeddings, memory systems, and custom tool integrations.

---

## 📂 Project Structure & Topics

| Topic / Folder                                                      | Description                                                                                                   |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| [**01_getting_started**](./01_getting_started/)                     | Basic introduction to LangChain and LangGraph. Building simple graphs and integrating with Gemini.            |
| [**02_tracing_and_observability**](./02_tracing_and_observability/) | How to trace agent executions, tool calls, and LLM responses using LangSmith.                                 |
| [**03_essay_writer_agent**](./03_essay_writer_agent/)               | An "Explain Like I'm 5" essay writing agent that searches the web and formats answers using a stateful graph. |
| [**04_types_of_runs**](./04_types_of_runs/)                         | Deep dive into LangSmith run types (LLM, Retriever, Tool, Chain, Prompt, Parser) and the `@traceable` decorator. |
| [**05_langsmith_studio**](./05_langsmith_studio/)                   | Using LangGraph Studio for visual debugging, time-travel, and step-by-step agent execution. |

---

## 🛠️ Environment Setup

To run the examples in this repository, you will need to set up your environment:

1. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. **Set up API Keys (`.env` file):**
   Create a `.env` file in the root directory with the following keys:

   ```env
   # LLM Providers
   GEMINI_API_KEY="your-gemini-api-key"
   OPENAI_API_KEY="your-openai-api-key" # Optional, if you use OpenAI models

   # Search Tools
   TAVILY_API_KEY="your-tavily-api-key"

   # LangSmith Tracing
   LANGCHAIN_TRACING_V2=true
   LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
   LANGCHAIN_PROJECT=langgraph-learn
   LANGCHAIN_API_KEY="your-langsmith-api-key"
   ```

3. **Install Dependencies:**
   Ensure you have the core packages installed (e.g., `langchain-core`, `langgraph`, `langchain-google-genai`, `tavily-python`, `python-dotenv`).
