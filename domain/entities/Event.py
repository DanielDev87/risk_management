from pydantic import BaseModel
    
class Event(BaseModel):
    id:int
    risk_type_id: int
    factor: str  
    descriptio: str
    probability_id: int
    impact_id: int