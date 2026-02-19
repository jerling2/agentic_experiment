from pydantic import BaseModel, Field


class SimpleState(BaseModel):
    input: str
    results: str = ""