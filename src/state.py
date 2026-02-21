from pydantic import BaseModel, Field


class InputState(BaseModel):
    thread_id: str | None = Field(
        default=None,
        description=(
            "Since this graph uses HTTP (stateless) transport protocol, include"
            "the thread_id to continue where you left off."
        )
    )


class OutputState(BaseModel):
    thread_id: str = Field(
        description=(
            "A thread_id is always returned as output. Reuse it in the " 
            "next invocation to continue the conversation."
        )
    )
    demo_result: str = ""


class NodeDemoState(BaseModel):
    success: bool = False
    demo_result: str = ""


class AppState(InputState, OutputState, NodeDemoState):
    pass
