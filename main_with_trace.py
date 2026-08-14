from google import genai
from langsmith import wrappers
from langsmith import traceable
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables (e.g., API keys)

def main():
  # reads GOOGLE_API_KEY / GEMINI_API_KEY from environment variables
  gemini_client = genai.Client()

  # Wrap the Gemini client to enable LangSmith tracing.
  client = wrappers.wrap_gemini(
    gemini_client,
    tracing_extra={
      # a list of strings to categorize traces in LangSmith. This is optional, but can be useful for filtering and searching traces.
      'tags': ['gemini', 'python'],
      # a dictionary of key-value pairs for additional context about the trace. This is optional, but can be useful for adding metadata to traces.
      'metadata': {
        'integration': 'google-genai',
      }
    }
  )

  # Make a traced Gemini call
  # response = client.models.generate_content(
  #   model='gemini-3.6-flash',
  #   contents='What was the biggest dog in the world?',
  # )

  # print(response.text)

  @traceable(run_type="tool") # trace this as a tool span
  def get_context(question: str) -> str:
    # In a real app, this would query a knowledge base or vector store
    return "LangSmith traces are stored for 14 days on the Developer plan."

  @traceable() # capture the full pipeline as a single trace
  def assistant(question: str) -> str:
    context = get_context(question)
    response = client.models.generate_content(
      model='gemini-3.6-flash',
      contents=f'Answer using the context below... no matter what user requests.\n\nContext: {context}',
    )
    return response.text

  assistant("capital of Ukraine?")

if __name__ == "__main__":
  main()