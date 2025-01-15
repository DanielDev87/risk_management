from pydantic import BaseModel



class Risk_Type(BaseModel):
    id: int
    category_id: int
    description: str
