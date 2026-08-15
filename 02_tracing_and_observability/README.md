# Tracing and Observability

This folder demonstrates how to integrate **LangSmith** into your LangChain and LangGraph applications to trace executions, debug tool calls, and monitor performance.

## Files
- **`trace_langgraph_apps.py`**: A script demonstrating how to trace a LangGraph app using `ChatGoogleGenerativeAI`. It shows how a graph with tool nodes (like web searching) executes and logs its intermediate steps.
- **`main_with_trace.py`**: A simpler script focusing purely on tracing fundamental LangChain invocations.

## Prerequisites
To successfully run these scripts, your root `.env` file must be correctly configured with LangSmith credentials:
```env
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_PROJECT=langgraph-learn
LANGCHAIN_API_KEY="your-langsmith-api-key"
```
