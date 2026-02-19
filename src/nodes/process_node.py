from langgraph.runtime import Runtime

from src import AppContext, SimpleState

def process_node(state: SimpleState, runtime: Runtime[AppContext]):
    desc = runtime.context.description
    user_input = state.input

    return {"results": f"context description {desc} and state.input {user_input}"}