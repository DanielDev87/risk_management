from sqlalchemy.orm import Session
from domain.entities.Product_Service import Product_Service

class SqlAchemyProductSRepository:
    def __init__(self, db:Session):
        self.db = db

    def create_productS(self, productService:Product_Service):
        db_productS = Product_Service(idProduct=Product_Service.id, description=Product_Service.descritcion)
        self.db.add(db_productS)
        self.db.commit()
        self.db.refresh(db_productS)
        return db_productS
    
    def get_productService(self, idProduct:int):
        return self.db.query(Product_Service).filter(ProductS.id== idProduct).first()
   