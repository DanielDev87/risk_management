from sqlalchemy.orm import Session
from infrastructure.orm.models import Cause

class SqlAlchemyCauseRpository:
    def __init__(self, db: Session):
        self.db = db
    def create_cause(self, cause:Cause):
        self.db.add(cause)
        self.db.commit()
        self.db.refresh(cause)
        return cause
    
    def get_cause(self, cause_id:int):
        return self.db.query(Cause).filter(Cause.id == cause_id).first()
    
    def get_all_cause(self):
        return self.db.query(Cause).all()
    
    def update_cause(self, cause:Cause):
        db_cause= self.db.query(Cause).filter(Cause.id == cause).first()
        db_cause.description=cause.description
        db_cause.risk_factor_id=cause.risk_factor_id
        db_cause.event_id=cause.event_id
        self.db.commit()
        self.db.refresh(db_cause)
        return db_cause
    
    def delete_cause(self, cause_id:int):
        db_cause = self.db.query(Cause).filter(Cause.id == cause_id).first()
        self.db.delete(db_cause)
        self.db.commit()
        return {"detail": "Cause deleted successfully"}