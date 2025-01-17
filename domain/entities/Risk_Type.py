from typing import Optional
from pydantic import BaseModel



class Risk_Type(BaseModel):
    id: Optional[int] = None
    category_id: int
    description: str
