from fastapi import APIRouter, HTTPException, Depends
from typing import List
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from infrastructure.database.db_config import get_db
from domain.repositories.cause_repository import CauseRepository
from application.use_cases.manage_causes import (
    create_cause,
    get_cause,
    get_all_causes,
    update_cause,
    delete_cause,
)

router = APIRouter()

class CauseCreate(BaseModel):
    description: str
    risk_factor_id: int
    event_id: int

class CauseResponse(BaseModel):
    id: int
    description: str
    risk_factor_id: int
    event_id: int


@router.post("/causes/", response_model=CauseResponse)
async def create_cause_endpoint(cause: CauseCreate, db: AsyncSession = Depends(get_db)):
    repository = CauseRepository(db)
    created_cause = await create_cause(cause, repository)
    return CauseResponse(**created_cause.dict())


@router.get("/causes/{cause_id}", response_model=CauseResponse)
async def read_cause_endpoint(cause_id: int, db: AsyncSession = Depends(get_db)):
    repository = CauseRepository(db)
    cause = await get_cause(cause_id, repository)
    if not cause:
        raise HTTPException(status_code=404, detail="Cause not found")
    return CauseResponse(**cause.dict())


@router.get("/causes/", response_model=List[CauseResponse])
async def read_all_causes_endpoint(db: AsyncSession = Depends(get_db)):
    repository = CauseRepository(db)
    causes = await get_all_causes(repository)
    return [CauseResponse(**c.dict()) for c in causes]


@router.put("/causes/{cause_id}", response_model=CauseResponse)
async def update_cause_endpoint(cause_id: int, cause: CauseCreate, db: AsyncSession = Depends(get_db)):
    repository = CauseRepository(db)
    updated_cause = await update_cause(cause_id, cause, repository)
    if not updated_cause:
        raise HTTPException(status_code=404, detail="Cause not found")
    return CauseResponse(**updated_cause.dict())


@router.delete("/causes/{cause_id}", response_model=dict)
async def delete_cause_endpoint(cause_id: int, db: AsyncSession = Depends(get_db)):
    repository = CauseRepository(db)
    await delete_cause(cause_id, repository)
    return {"detail": "Cause deleted"}
