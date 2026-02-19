# 📦 LangGraph
from langgraph.graph import StateGraph, START, END
from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime

from src.nodes import process_node
from src.state import SimpleState
from src.context import AppContext

builder = StateGraph(state_schema=SimpleState, context_schema=AppContext)
builder.add_node("demo_node", process_node)
builder.add_edge(START, "demo_node")
builder.add_edge("demo_node", END)

graph = builder.compile()