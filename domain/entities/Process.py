from pydantic import BaseModel

class Process(BaseModel):
    id: int
    macroprocess_id: int
    description: str