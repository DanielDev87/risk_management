from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import insert, update, delete
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
from infrastructure.orm.models import RiskControlType
from domain.entities.Risk_Control_Types import Risk_Control_Types


class RiskControlTypeRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_risk_control_type(self, control_type: Risk_Control_Types) -> Risk_Control_Types:
        stmt = insert(RiskControlType).values(
            description=control_type.description
        ).returning(RiskControlType.id, RiskControlType.description)

        try:
            result = await self.session.execute(stmt)
            await self.session.commit()
            row = result.fetchone()
            if row:
                return Risk_Control_Types(id=row.id, description=row.description)
        except IntegrityError as e:
            await self.session.rollback()
            raise ValueError("Risk Control Type already exists") from e

    async def get_risk_control_type(self, control_type_id: int) -> Optional[Risk_Control_Types]:
        stmt = select(RiskControlType).where(RiskControlType.id == control_type_id)
        result = await self.session.execute(stmt)
        control_type = result.scalar_one_or_none()
        if control_type:
            return Risk_Control_Types(id=control_type.id, description=control_type.description)
        return None

    async def get_all_risk_control_types(self) -> List[Risk_Control_Types]:
        stmt = select(RiskControlType)
        result = await self.session.execute(stmt)
        control_types = result.scalars().all()
        return [Risk_Control_Types(id=ct.id, description=ct.description) for ct in control_types]

    async def update_risk_control_type(self, control_type_id: int, control_type: Risk_Control_Types) -> Optional[Risk_Control_Types]:
        stmt = update(RiskControlType).where(RiskControlType.id == control_type_id).values(
            description=control_type.description
        ).returning(RiskControlType.id, RiskControlType.description)

        result = await self.session.execute(stmt)
        await self.session.commit()
        row = result.fetchone()
        if row:
            return Risk_Control_Types(id=row.id, description=row.description)
        return None

    async def delete_risk_control_type(self, control_type_id: int) -> None:
        stmt = delete(RiskControlType).where(RiskControlType.id == control_type_id)
        result = await self.session.execute(stmt)
        await self.session.commit()
        if result.rowcount == 0:
            raise ValueError(f"Risk Control Type with id {control_type_id} not found")
