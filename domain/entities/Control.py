from pydantic import BaseModel, Field
from typing import Optional

class Control(BaseModel):
    id: int 
    control_type_id: int 
    description: str 
    frequency: Optional[str] 
    responsible_id: int
