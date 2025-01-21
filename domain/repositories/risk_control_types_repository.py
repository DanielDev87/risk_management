from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import insert, update, delete
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
from infrastructure.orm.models import RiskControlType
from domain.entities.Risk_Control_Types import Risck_Control_Type

class RiskControlTypeRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def create_risk_control_type(self, riskcontroltype:Risck_Control_Type)-> Risck_Control_Type:
        stmt= insert(RiskControlType).values(
            description=riskcontroltype.description
        ).returning(RiskControlType.id, RiskControlType.description)
        
        try:
            result = await self.session.execute(stmt)
            await self.session.commit()
            row=result.fetchone()
            if row:
                return Risck_Control_Type(id=row.id, description=row.description)
        except IntegrityError as e:
            await self.session.rollback()
            raise ValueError("Risk Control Type with this description already exists or invalid category ID") from e
        
    
    async def get_risk_control_type(self, risk_control_type_id:int) -> Optional [Risck_Control_Type]:
        stmt = select(RiskControlType).where(RiskControlType.id == risk_control_type_id)
        result= await self.db.execute(stmt)
        risk_control_type= result.scalar_one_or_none()
        if risk_control_type:
            return Risck_Control_Type(
                id=risk_control_type.id, 
                description=risk_control_type.description
            )
        return None
    
    