from typing import Optional
from pydantic import BaseModel

class Risk_Control_Types(BaseModel):
    id: Optional [int] = None
    description: str