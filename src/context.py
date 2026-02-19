from pydantic import BaseModel

class AppContext(BaseModel):
    description: str = "default description"