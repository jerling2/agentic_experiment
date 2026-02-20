# 📦 LangGraph
from langgraph.graph import StateGraph, START, END


# 🧠 Source code
from src.nodes import demo_node
from src.state import InputState, OutputState, AppState
from src.context import AppContext


# Configuration
builder = StateGraph(
    input_schema=InputState, 
    output_schema=OutputState, 
    state_schema=AppState,
    context_schema=AppContext
)


# Nodes
builder.add_node("demo_node", demo_node)


# Edges
builder.add_edge(START, "demo_node")
builder.add_edge("demo_node", END)


# Graph
graph = builder.compile()
