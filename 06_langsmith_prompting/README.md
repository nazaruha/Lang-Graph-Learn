# LangSmith Prompts & Playground

LangSmith provides a built-in **Playground** where you can test, edit, and experiment with your prompts using different LLMs. 

Once a prompt is created and tested, it is saved in the **Prompts** tab (often informally referred to as a "Prompt Hub"). LangSmith automatically tracks versions and commits for your prompts, allowing you to dynamically pull them directly into your Python code.

### Why is this useful?
- **No hardcoded prompts:** You don't need to clutter your codebase with massive, multi-line string prompts.
- **Dynamic Updates:** You can tweak and update the prompt in the LangSmith UI, and your application will immediately start using the new version without needing to deploy new code.
- **Version Control:** You can easily track changes and roll back to previous prompt versions if an update degrades performance.

## How to pull a prompt into your code

1. **Set your API Key:** Ensure you have your `LANGSMITH_API_KEY` set in your environment variables (usually via `.env`).
2. **Pull the prompt:** Use the `langsmith.Client` to pull your specific prompt by its name.

```python
import os
from langsmith import Client

# Initialize the client
client = Client()

# Pull the prompt by its name in the LangSmith Prompts tab
prompt = client.pull_prompt(
    "essay_5yo_consice",
    include_model=True,
    secrets={"OPENAI_API_KEY": os.getenv("OPENAI_API_KEY")}
)
```
