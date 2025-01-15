from pydantic import BaseModel

class Macroprocess(BaseModel):
    id: int
    description: str