from pydantic import BaseModel, Field
from typing import Optional

class Personal(BaseModel):
    id: Optional[int] = None
    name: str 
    position: str 
    area: Optional[str] 
    process_id: Optional[int] 
    email: Optional[str] 