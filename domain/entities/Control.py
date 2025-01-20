from pydantic import BaseModel, Field
from typing import Optional

class Control(BaseModel):
    id: Optional[int] = None
    control_type_id: int 
    description: str 
    frequency: Optional[str] 
    responsible_id: int
