from pydantic import BaseModel

class Risk_Factor(BaseModel):
    id: int
    risk_type_id: int
    description: str