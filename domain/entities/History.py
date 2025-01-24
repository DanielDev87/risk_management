from pydantic import BaseModel
from typing import Optional
from datetime import datetime
    
class History(BaseModel):
    id: Optional[int] = None
    eventlog_id: int
    control_id: int  
    start_date: datetime
    end_date: Optional[datetime] 
    value_risk: float