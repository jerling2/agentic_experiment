from pydantic import BaseModel

"""
TODO: Define the static-state (context) of the graph
e.g.,
# Identity and Behavior
- System Prompt (instructions)
- Role or Persona
- Tone/Style guidelines
# Execution Configuration
- Model Name - Model Paramaters (temp, max toks)
# 


"""
class AppContext(BaseModel):
    name: str = "Demo"
