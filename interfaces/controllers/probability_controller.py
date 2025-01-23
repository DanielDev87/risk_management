from fastapi import APIRouter, HTTPException, Depends
from typing import List
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from infrastructure.database.db_config import get_db
from domain.repositories.probability_repository import ProbabilityRepository
from application.use_cases.manage_probabilities import (
    create_probability,
    get_probability,
    get_all_probabilities,
    update_probability,
    delete_probability,
)

router = APIRouter()

class ProbabilityCreate(BaseModel):
    level: int
    description: str
    definition: str
    criteria_percentage: int

class ProbabilityResponse(BaseModel):
    id: int
    level: int
    description: str
    definition: str
    criteria_percentage: int


@router.post("/probabilities/", response_model=ProbabilityResponse)
async def create_probability_endpoint(probability: ProbabilityCreate, db: AsyncSession = Depends(get_db)):
    repository = ProbabilityRepository(db)
    created_probability = await create_probability(probability, repository)
    return ProbabilityResponse(**created_probability.model_dump())


@router.get("/probabilities/{probability_id}", response_model=ProbabilityResponse)
async def read_probability_endpoint(probability_id: int, db: AsyncSession = Depends(get_db)):
    repository = ProbabilityRepository(db)
    probability = await get_probability(probability_id, repository)
    if not probability:
        raise HTTPException(status_code=404, detail="Probability not found")
    return ProbabilityResponse(**probability.model_dump())


@router.get("/probabilities/", response_model=List[ProbabilityResponse])
async def read_all_probabilities_endpoint(db: AsyncSession = Depends(get_db)):
    repository = ProbabilityRepository(db)
    probabilities = await get_all_probabilities(repository)
    return [ProbabilityResponse(**p.model_dump()) for p in probabilities]


@router.put("/probabilities/{probability_id}", response_model=ProbabilityResponse)
async def update_probability_endpoint(probability_id: int, probability: ProbabilityCreate, db: AsyncSession = Depends(get_db)):
    repository = ProbabilityRepository(db)
    updated_probability = await update_probability(probability_id, probability, repository)
    if not updated_probability:
        raise HTTPException(status_code=404, detail="Probability not found")
    return ProbabilityResponse(**updated_probability.model_dump())


@router.delete("/probabilities/{probability_id}", response_model=dict)
async def delete_probability_endpoint(probability_id: int, db: AsyncSession = Depends(get_db)):
    repository = ProbabilityRepository(db)
    await delete_probability(probability_id, repository)
    return {"detail": "Probability deleted"}
