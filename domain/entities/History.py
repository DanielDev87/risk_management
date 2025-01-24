from pydantic import BaseModel
from typing import Optional
from datetime import datetime
    
class History(BaseModel):
<<<<<<< HEAD
    id:int
=======
    id: Optional[int] = None
>>>>>>> b45a91bcf58cd148abbdda1f7b4a3e2c301d6b86
    eventlog_id: int
    control_id: int  
    start_date: datetime
    end_date: Optional[datetime] 
    value_risk: float