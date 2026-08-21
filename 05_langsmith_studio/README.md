# LangGraph Studio

LangGraph Studio is a beautiful visual debugging interface for your LangGraph agents. While you can build agents without it, Studio is an incredibly important tool—especially when working with complex agent logic or cyclical workflows—because it makes debugging significantly more comfortable.

With LangGraph Studio, you can:
- **Visualize** the graph structure and follow the workflow step-by-step.
- **Interrupt** the execution at any point.
- **Fork and Edit:** Modify the state or edit a node, and re-execute the flow starting from that exact point (time-travel).

## How to Run

1. **Install the CLI:**
   If you don't have Docker installed, use the in-memory server option:
   ```bash
   pip install -U "langgraph-cli[inmem]"
   ```

2. **Configure API Keys:**
   Make sure your `.env` file contains your `LANGSMITH_API_KEY` (or `LANGCHAIN_API_KEY`).

3. **Configure `langgraph.json`:**
   The Studio will not work without a configuration file telling it where to find your compiled graph. You must create a `langgraph.json` file in the root of your project:
   ```json
   {
     "dependencies": ["."],
     "env": "./.env",
     "graph": {
       "My Agent Name": "./path/to/file.py:compiled_graph_variable"
     }
   }
   ```

4. **Start the Studio:**
   Open your terminal in the root of the repository (where the `langgraph.json` configuration file is located) and run:
   ```bash
   langgraph dev
   ```
   Click the URL provided in the terminal to open the Studio in your browser!
