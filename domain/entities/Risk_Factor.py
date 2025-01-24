from typing import Optional
from pydantic import BaseModel

class Risk_Factor(BaseModel):
    id: Optional[int] = None
    risk_type_id: int
    description: str