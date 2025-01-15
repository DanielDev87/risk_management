from pydantic import BaseModel

class Product_Service(BaseModel):
    id: int
    description: str