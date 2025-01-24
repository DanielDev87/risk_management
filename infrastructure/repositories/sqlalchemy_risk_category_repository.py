from sqlalchemy.orm import Session
from infrastructure.orm.models import RiskCategory

class SqlAlchemyRiskCategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_risk_category(self, risk_category: RiskCategory):
        self.db.add(risk_category)
        self.db.commit()
        self.db.refresh(risk_category)
        return risk_category
    
    def get_risk_category(self, category_id: int):
        return self.db.query(RiskCategory).filter(RiskCategory.id == category_id).first()
    
    def get_all_risk_categories(self):
        return self.db.query(RiskCategory).all()
    
    def update_risk_category(self, risk_category: RiskCategory):
        db_category = self.db.query(RiskCategory).filter(RiskCategory.id == risk_category.id).first()
        db_category.description = risk_category.description
        self.db.commit()
        self.db.refresh(db_category)
        return db_category
    
    def delete_risk_category(self, category_id: int):
        db_category = self.db.query(RiskCategory).filter(RiskCategory.id == category_id).first()
        self.db.delete(db_category)
        self.db.commit()
        return {"detail": "Risk category deleted successfully"}
