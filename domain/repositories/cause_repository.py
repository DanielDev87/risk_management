from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import insert, update, delete
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
from infrastructure.orm.models import Cause
<<<<<<< HEAD
from domain.entities.Cause import Cause
=======
from domain.entities.Cause import Cause as CauseEntity

>>>>>>> b4a58c63b1306a0bb223bffc5bc4961996ba2352

class CauseRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
<<<<<<< HEAD
    
async def create_cause(self, cause: Cause) -> Cause:
    stmt=insert(Cause).values(
        id=cause.id,
        description=cause.description,
        risk_factor_id=cause.risk_factor_id,
        event_id=cause.event_id
    ).returning(Cause.id, Cause.description, Cause.risk_factor_id, Cause.event_id)
    
    try:
=======

    async def create_cause(self, cause: CauseEntity) -> CauseEntity:
        stmt = insert(Cause).values(
            description=cause.description,
            risk_factor_id=cause.risk_factor_id,
            event_id=cause.event_id
        ).returning(
            Cause.id,
            Cause.description,
            Cause.risk_factor_id,
            Cause.event_id
        )

        try:
            result = await self.session.execute(stmt)
            await self.session.commit()
            row = result.fetchone()
            if row:
                return CauseEntity(
                    id=row.id,
                    description=row.description,
                    risk_factor_id=row.risk_factor_id,
                    event_id=row.event_id
                )
        except IntegrityError as e:
            await self.session.rollback()
            raise ValueError("Cause already exists") from e

    async def get_cause(self, cause_id: int) -> Optional[CauseEntity]:
        stmt = select(Cause).where(Cause.id == cause_id)
        result = await self.session.execute(stmt)
        cause = result.scalar_one_or_none()
        if cause:
            return CauseEntity(
                id=cause.id,
                description=cause.description,
                risk_factor_id=cause.risk_factor_id,
                event_id=cause.event_id
            )
        return None

    async def get_all_causes(self) -> List[CauseEntity]:
        stmt = select(Cause)
        result = await self.session.execute(stmt)
        causes = result.scalars().all()
        return [
            CauseEntity(
                id=c.id,
                description=c.description,
                risk_factor_id=c.risk_factor_id,
                event_id=c.event_id
            ) for c in causes
        ]

    async def update_cause(self, cause_id: int, cause: CauseEntity) -> Optional[CauseEntity]:
        stmt = update(Cause).where(Cause.id == cause_id).values(
            description=cause.description,
            risk_factor_id=cause.risk_factor_id,
            event_id=cause.event_id
        ).returning(
            Cause.id,
            Cause.description,
            Cause.risk_factor_id,
            Cause.event_id
        )

>>>>>>> b4a58c63b1306a0bb223bffc5bc4961996ba2352
        result = await self.session.execute(stmt)
        await self.session.commit()
        row = result.fetchone()
        if row:
<<<<<<< HEAD
            return Cause(id=row.id, decripcion=row.descripcion, risk_factor_id=row.risk_factor_id,event_id=row.event_id)
    except IntegrityError as e:
        await self.session.rollback()
        raise ValueError("The Cause already exists or invalid category ID") from e
    
async def get_cause(self, cause_id:int)-> Optional [Cause]:
    stmt = select(Cause).where(Cause.id == cause_id)
    result= await self.session.execute(stmt)
    cause=result.scalar_one_or_none()
    if cause:
        return Cause(
            id=cause.id, 
            description=cause.description, 
            risk_factor_id=cause.risk_factor_id,
            event_id=cause.event_id
        )
    return None

async def get_all_cause(self)-> list[Cause]:
    stmt = select(Cause)
    result = await self.session.execute(stmt)
    causes = result.scalars().all()
    return [
        Cause(
            id=cause.id, 
            description=cause.description, 
            risk_factor_id=cause.risk_factor_id,
            event_id=cause.event_id)
        for cause in causes
    ]
    
async def update_cause(self,cause_id:int, case:Cause)-> Optional[Cause]:
    stmt = update(Cause).where(Cause.id == cause_id).values(
        description=case.description,
        risk_factor_id=case.risk_factor_id,
        event_id=case.event_id
    ).returning(Cause.description, Cause.risk_factor_id, Cause.event_id)
    
    result= await self.session.execute(stmt)
    await self.session.commit()
    row= result.fetchone()
    if row:
        return Cause(id=row.id, description=row.description, event_id=row.event_id)
    return None

async def delete_cause(self, cause_id:int)->None:
    stmt = delete(Cause).where(Cause.id == cause_id)
    result= await self.session.execute(stmt)
    await self.session.commit()
    if result.rowcount==0:
        raise ValueError(f"Cause with id {cause_id} not found")
=======
            return CauseEntity(
                id=row.id,
                description=row.description,
                risk_factor_id=row.risk_factor_id,
                event_id=row.event_id
            )
        return None

    async def delete_cause(self, cause_id: int) -> None:
        stmt = delete(Cause).where(Cause.id == cause_id)
        result = await self.session.execute(stmt)
        await self.session.commit()
        if result.rowcount == 0:
            raise ValueError(f"Cause with id {cause_id} not found")
>>>>>>> b4a58c63b1306a0bb223bffc5bc4961996ba2352
