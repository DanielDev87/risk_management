from domain.entities.Cause import Cause
from domain.repositories.cause_repository import CauseRepository


async def create_cause(cause_data: Cause, repository: CauseRepository) -> Cause:
    return await repository.create_cause(cause_data)


async def get_cause(cause_id: int, repository: CauseRepository) -> Cause:
    return await repository.get_cause(cause_id)


async def get_all_causes(repository: CauseRepository) -> list[Cause]:
    return await repository.get_all_causes()


async def update_cause(cause_id: int, cause_data: Cause, repository: CauseRepository) -> Cause:
    return await repository.update_cause(cause_id, cause_data)


async def delete_cause(cause_id: int, repository: CauseRepository) -> None:
    await repository.delete_cause(cause_id)
