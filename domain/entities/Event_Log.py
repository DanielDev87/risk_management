from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EventLog(BaseModel):
    id: Optional[int]=None
    event_code: Optional[str] 
    start_date: datetime 
    end_date: Optional[datetime] 
    discovery_date: Optional[datetime] 
    accounting_date: Optional[datetime]
    amount: Optional[float] 
    recovered_amount: Optional[float] 
    insurance_recovery: Optional[float] 
    risk_factor_id: Optional[int] 
    product_id: Optional[int] 
    process_id: Optional[int] 
    channel_id: Optional[int] 
    city: Optional[str] 
    responsible_id: Optional[int] 
    status: Optional[str] 