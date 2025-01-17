from infrastructure.database.db_config import SessionLocal
from infrastructure.repositories.sqlalchemy_products_repository import SqlAchemyProductSRepository
from application.use_cases.create_event_products import create_productS
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Funcion para la ruta /productos-servicios
@router.post("/products/")
def create_new_product(idProduct:int, description:str, db:Session = Depends(get_db)):
    repository = SqlAchemyProductSRepository(db)
    product = create_productS(idProduct, description, repository)
    return product

