from pydantic import BaseModel
from typing import Optional
from datetime import datetime
    
class History(BaseModel):
    id:int
    eventlog_id: int
    control_id: int  
    start_date: datetime
    end_date: Optional[datetime] 
    value_risk: float