# Creation of "Types of Runs" while tracing a LangSmith

This will help you to understand the application's execution. LangSmith supports many different types of Runs - you can specify what type your Run in the **@traceable** decorator.

## The types of runs are:

- **LLM:** Invokes an LLM
- **Retriever:** Retrieves documents from DBs or other sources
- **Tool:** Executes actions with function calls
- **Chain:** Default Run type; combines multiple Runs into a larger process
- **Prompt:** Hydrates a prompt to be used with an LLM
- **Parser:** Extracts structured data
