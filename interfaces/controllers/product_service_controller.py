from fastapi import APIRouter, HTTPException, Depends
from typing import List
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from infrastructure.database.db_config import get_db
from domain.repositories.product_service_repository import ProductServiceRepository 
from domain.entities.Product_Service import Product_Service

router = APIRouter()

class ProductServiceCreate(BaseModel):
    description: str

class ProductServiceResponse(BaseModel):
    id: int
    description: str

@router.post("/products_services/", response_model=ProductServiceResponse)
async def create_product_service(product_service: ProductServiceCreate, db: AsyncSession = Depends(get_db)):
    repository = ProductServiceRepository(db)
    created_product_service = await repository.create_product_service(Product_Service(description=product_service.description))
    return ProductServiceResponse(id=created_product_service.id, description=created_product_service.description)

@router.get("/products_services/{product_service_id}", response_model=ProductServiceResponse)
async def read_product_service(product_service_id: int, db: AsyncSession = Depends(get_db)):
    repository = ProductServiceRepository(db)
    product_service = await repository.get_product_service(product_service_id)
    if product_service is None:
        raise HTTPException(status_code=404, detail="Product_Service not found")
    return ProductServiceResponse(id=product_service.id, description=product_service.description)

@router.get("/products_services/", response_model=List[ProductServiceResponse])
async def read_products_services(db: AsyncSession = Depends(get_db)):
    repository = ProductServiceRepository(db)
    products_services = await repository.get_all_products_services()
    return [ProductServiceResponse(id=ps.id, description=ps.description) for ps in products_services]

@router.put("/products_services/{product_service_id}", response_model=ProductServiceResponse)
async def update_product_service(product_service_id: int, product_service: ProductServiceCreate, db: AsyncSession = Depends(get_db)):
    repository = ProductServiceRepository(db)
    updated_product_service = await repository.update_product_service(product_service_id, Product_Service(description=product_service.description))
    if updated_product_service is None:
        raise HTTPException(status_code=404, detail="Product_Service not found")
    return ProductServiceResponse(id=updated_product_service.id, description=updated_product_service.description)

@router.delete("/products_services/{product_service_id}", response_model=dict)
async def delete_product_service(product_service_id: int, db: AsyncSession = Depends(get_db)):
    repository = ProductServiceRepository(db)
    await repository.delete_product_service(product_service_id)
    return {"detail": "Product_Service deleted"}
