from fastapi import APIRouter, HTTPException, Depends
from typing import List
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from infrastructure.database.db_config import get_db
from domain.repositories.cause_reository import CauseRepository
from application.use_cases.manage_cause import (
    create_cause,
    get_cause,
    get_all_cause,
    update_cause,
    delete_cause,
)

router = APIRouter()

class CauseCreate(BaseModel):
    description: str
    risk_factor_id:int
    event_id:int

class CauseResponse(BaseModel):
    id: int
    description: str
    risk_factor_id: int
    event_id: int
    
@router.post("/cause/", response_model=CauseResponse)
async def create_cause_endpoint(cause:CauseCreate, db: AsyncSession = Depends(get_db)):
    repository=CauseRepository(db)
    created_cause=await create_cause(cause, repository)
    return CauseResponse(
        id=created_cause.id,
        description=created_cause.description,
        risk_factor_id=created_cause.risk_factor_id,
        event_id=created_cause.event_id
    )

@router.get("/cause/{cause_id}", response_model=CauseResponse)
async def read_cause_endpoint(self, cause_id:int,  db:AsyncSession = Depends(get_db)):
    repository=CauseRepository(db)
    cause=await get_cause(cause_id, repository)
    if not cause:
        raise HTTPException(status_code=404, detail="Cause not found")
    return CauseResponse(
        id=cause.id,
        description=cause.description,
        risk_factor_id=cause.risk_factor_id,
        event_id=cause.event_id
    )
    
@router.get("/cause/", response_model=List[CauseResponse])
async def read_all_cause_endpoint(db: AsyncSession = Depends(get_db)):
    repository=CauseRepository(db)
    causes=await get_all_cause(repository)
    return[
        CauseResponse(
            id=cause.id,
            description=cause.description,
            risk_factor_id=cause.risk_factor_id,
            event_id=cause.event_id
        )
        for cause in causes
    ]
    
@router.put("/cause/{cause_id}", response_model=CauseResponse)
async def update_cause_endpoint(cause_id: int, cause: CauseCreate, db: AsyncSession = Depends(get_db)):
    repository = CauseRepository(db)
    updated_cause = await update_cause(cause_id, cause, repository)
    if not updated_cause:
        raise HTTPException(status_code=404, detail="Cause not found")
    return CauseResponse(
        id=updated_cause.id,
        description=updated_cause.description,
        risk_factor_id=updated_cause.risk_factor_id,
        event_id=updated_cause.event_id
    )

@router.delete("/cause/{cause_id}", response_model=dict)
async def delete_cause_endpoint(cause_id: int, db: AsyncSession = Depends(get_db)):
    repository = CauseRepository(db)
    await delete_cause(cause_id, repository)
    return {"detail": "Cause deleted"}
