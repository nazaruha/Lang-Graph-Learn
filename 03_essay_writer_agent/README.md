# Essay Writer Agent ("Explain Like I'm 5")

This folder contains the implementation of a research and writing agent. Given a complex topic, the agent searches the web for context and then uses an LLM to explain the concept simply, as if speaking to a 5-year-old.

## Files
- **`essay_writer_5_yo.ipynb`**: The initial prototype. It demonstrates defining the tools (Tavily search) and the LLM prompts as plain Python functions without a formal graph structure.
- **`essay_writer_5_yo_langgraph.ipynb`**: The refactored version of the same agent, implemented formally using **LangGraph**. It defines a `GraphState`, separate nodes for searching and explaining, and compiles them into a visualizable state machine.

## Prerequisites
Make sure your root `.env` file contains valid keys for both the LLM and the search tool:
- `GEMINI_API_KEY` or `OPENAI_API_KEY`
- `TAVILY_API_KEY`
