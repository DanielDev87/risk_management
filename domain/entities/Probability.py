from pydantic import BaseModel

class Process(BaseModel):
    id: int
    level: int
    description: str
    definition: str
    criteria_percentage: int

