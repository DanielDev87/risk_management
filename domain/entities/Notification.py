from pydantic import BaseModel
from datetime import datetime
    
class Notification(BaseModel):
    id:int
    message: str  
    suggestion_control: str
    date_send: datetime
    user_id: int
    eventlog_id: int