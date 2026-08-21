from langchain_openai import ChatOpenAI
from tavily import TavilyClient
from typing import TypedDict, List
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv
import os

_ = load_dotenv(override=True, dotenv_path='.env')
llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

class InputState(TypedDict):
  question: str

class GraphState(TypedDict):
  question: str
  messages: List[str]
  documents: List[str]

def _get_state(state: GraphState):
  return {"question": state["question"], "documents": state.get("documents", []), "messages": state.get("messages", [])}

prompt = """You are a professor and expert in explaining complex topics in a way that is easy to understand.
Your job is to answer the provided question so that even a 5 year old can understand it.
You have provided with relevant background context to answer the question.

Question: {question}

Context: {context}

Answer:"""

def search(state: GraphState):
  """
  Web search based on the re-phrased question.

  Args:
    state (dict): The current graph state
  
  Returns:
    state (dict): Updates documents key with appended web results
  """

  _state = _get_state(state)

  web_response = tavily.search(query=_state["question"], max_results=2)
  web_results = "\n".join([r['content'] for r in web_response['results']])
  web_results = Document(page_content=web_results)
  _state["documents"].append(web_results)

  return {"question": _state["question"], "documents": _state["documents"]}

def explain(state: GraphState):
  """
  Generate response

  Args:
    state (dict): The current graph state

  Returns:
    state (dict): New key added to state, generation, that contains LLM generation
  """

  _state = _get_state(state)

  formatted = prompt.format(question=_state["question"], context="\n".join([d.page_content for d in _state["documents"]]))
  generation = llm.invoke([HumanMessage(content=formatted)])

  return {"question": _state["question"], "messages": [generation]}

graph = StateGraph(GraphState, input_schema=InputState)
graph.add_node("explain", explain)
graph.add_node("search", search)
graph.add_edge(START, "search")
graph.add_edge("search", "explain"),
graph.add_edge("explain", END)

essay_writer_5_yo = graph.compile()

