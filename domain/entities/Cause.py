from pydantic import BaseModel, Field
from typing import Optional

class Cause(BaseModel):
    id: Optional[int] = None 
    description: str 
    risk_factor_id: int 
    event_id: int 