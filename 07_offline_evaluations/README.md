# Offline Evaluations with LangSmith

Offline evaluation is the practice of systematically testing and benchmarking your AI application against curated datasets before deploying changes.

## Core Concepts

- **Dataset:** A collection of benchmark examples containing sample inputs and optional reference (ground-truth) outputs.
- **Evaluators:** Functions that assess and score the application's outputs:
  - **Deterministic Code Evaluators:** Fast, rule-based checks for closed-ended criteria (e.g., length/word count, JSON validity, regex).
  - **LLM-as-a-Judge Evaluators:** Using an LLM with structured outputs to score open-ended criteria against a rubric (e.g., factual accuracy, logical consistency).
- **Experiments:** Running your pipeline over a dataset with `langsmith.evaluate()` to log metrics, compare model performance, and track regressions directly in LangSmith.

## How It Works

```python
from langsmith import evaluate

# 1. Target function that runs your application
def run(inputs: dict):
    return main(inputs["question"])

# 2. Evaluators (Code-based & LLM-as-a-Judge)
# - conciseness: deterministic check
# - correctness: LLM rubric evaluation against reference outputs

# 3. Run evaluation experiment
evaluate(
    run,
    data="essay-writer-5yo",
    evaluators=[correctness, conciseness],
    experiment_prefix="eli5-experiment"
)
```
