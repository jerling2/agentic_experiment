from langgraph.runtime import Runtime
from src.state import AppState, NodeDemoState
from src.context import AppContext


def demo_node(state: AppState, runtime: Runtime[AppContext]) -> NodeDemoState:
    result_str = f"Thread_id: {state.thread_id}, context.name {runtime.context.name}"
    return NodeDemoState(success=True, demo_result=result_str)
