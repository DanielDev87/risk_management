from pydantic import BaseModel

class Channel(BaseModel):
    id: int
    description: str