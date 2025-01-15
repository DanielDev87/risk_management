from pydantic import BaseModel

class Risk_Category(BaseModel):
    id: int
    description: str