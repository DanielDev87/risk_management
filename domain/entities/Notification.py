<<<<<<< HEAD
=======
from typing import Optional
>>>>>>> b45a91bcf58cd148abbdda1f7b4a3e2c301d6b86
from pydantic import BaseModel
from datetime import datetime
    
class Notification(BaseModel):
<<<<<<< HEAD
    id:int
=======
    id: Optional[int] = None
>>>>>>> b45a91bcf58cd148abbdda1f7b4a3e2c301d6b86
    message: str  
    suggestion_control: str
    date_send: datetime
    user_id: int
    eventlog_id: int