from typing import Optional
from pydantic import BaseModel

class Channel(BaseModel):
    id: Optional[int] = None
    description: str