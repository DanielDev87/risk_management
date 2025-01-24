from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import insert, update, delete
from typing import List, Optional
from domain.entities.Product_Service import Product_Service
from infrastructure.orm.models import ProductService as ORMProductService

class ProductServiceRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_product_service(self, product_service: Product_Service) -> Product_Service:
        stmt = insert(ORMProductService).values(description=product_service.description).returning(ORMProductService.id, ORMProductService.description)
        result = await self.session.execute(stmt)
        await self.session.commit()
        row = result.fetchone()
        if row:
            return Product_Service(id=row.id, description=row.description)

    async def get_product_service(self, product_service_id: int) -> Optional[Product_Service]:
        stmt = select(ORMProductService).where(ORMProductService.id == product_service_id)
        result = await self.session.execute(stmt)
        orm_product_service = result.scalar_one_or_none()
        if orm_product_service:
            return Product_Service(id=orm_product_service.id, description=orm_product_service.description)
        return None

    async def get_all_products_services(self) -> List[Product_Service]:
        stmt = select(ORMProductService)
        result = await self.session.execute(stmt)
        orm_product_services = result.scalars().all()
        return [Product_Service(id=ps.id, description=ps.description) for ps in orm_product_services]

    async def update_product_service(self, product_service_id: int, product_service: Product_Service) -> Optional[Product_Service]:
        stmt = update(ORMProductService).where(ORMProductService.id == product_service_id).values(description=product_service.description).returning(ORMProductService.id, ORMProductService.description)
        result = await self.session.execute(stmt)
        await self.session.commit()
        row = result.fetchone()
        if row:
            return Product_Service(id=row.id, description=row.description)
        return None

    async def delete_product_service(self, product_service_id: int) -> None:
        stmt = delete(ORMProductService).where(ORMProductService.id == product_service_id)
        result = await self.session.execute(stmt)
        await self.session.commit()
        if result.rowcount == 0:
            raise ValueError(f"Product_Service with id {product_service_id} not found")
