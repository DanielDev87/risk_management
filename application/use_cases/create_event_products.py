from domain.entities.Product_Service import Product_Service
from infrastructure.repositories.sqlalchemy_products_repository import SqlAchemyProductSRepository

def create_productS(idProduct:int, description:str, repository:SqlAchemyProductSRepository):
    products = Product_Service(id=idProduct, description=description)    
    return repository.create_productS(products)