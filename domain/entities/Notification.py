from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Notification(BaseModel):
    id: int 
    message: str 
    suggestion_control: Optional[str] 
    date_sent: datetime 
    user_id: int 
    event_id: int 