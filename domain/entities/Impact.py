from pydantic import BaseModel

class Impact(BaseModel):
    id: int
    level: int
    description: str
    definition: str
    criteria_smlv: int