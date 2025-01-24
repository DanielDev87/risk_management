from typing import Optional
from pydantic import BaseModel

class Product_Service(BaseModel):
    id: Optional[int]=None
    description: str