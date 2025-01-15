from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Tracking(BaseModel):
    id: int 
    user_id: int 
    control_id: int 
    event_id: int 
    tracking_date: datetime 