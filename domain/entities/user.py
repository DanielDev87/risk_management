from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    username: str
    password: str
    role_id: int
    created_at: Optional[str] = None
    updated_at: Optional[str] = None