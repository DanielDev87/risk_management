from typing import Optional
from pydantic import BaseModel

<<<<<<< HEAD
class Risck_Control_Type(BaseModel):
    id: int
=======
class Risk_Control_Types(BaseModel):
    id: Optional [int] = None
>>>>>>> b4a58c63b1306a0bb223bffc5bc4961996ba2352
    description: str