from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import insert, update, delete
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
from infrastructure.orm.models import User as ORMUser
from domain.entities.user import User

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(self, user: User) -> User:
        stmt = insert(ORMUser).values(
            username=user.username, 
            password=user.password, 
            role_id=user.role_id
        ).returning(ORMUser.id, ORMUser.username, ORMUser.role_id)
        try:
            result = await self.session.execute(stmt)
            await self.session.commit()
            row = result.fetchone()
            if row:
                return User(id=row.id, username=row.username, password=user.password, role_id=row.role_id)
        except IntegrityError as e:
            await self.session.rollback()
            raise ValueError("User with this username already exists") from e

    async def get_user(self, user_id: int) -> Optional[User]:
        stmt = select(ORMUser).where(ORMUser.id == user_id)
        result = await self.session.execute(stmt)
        orm_user = result.scalar_one_or_none()
        if orm_user:
            return User(id=orm_user.id, username=orm_user.username, password=orm_user.password, role_id=orm_user.role_id)
        return None

    async def get_all_users(self) -> List[User]:
        stmt = select(ORMUser)
        result = await self.session.execute(stmt)
        orm_users = result.scalars().all()
        return [User(id=u.id, username=u.username, password=u.password, role_id=u.role_id) for u in orm_users]

    async def update_user(self, user_id: int, user: User) -> Optional[User]:
        stmt = update(ORMUser).where(ORMUser.id == user_id).values(
            username=user.username, 
            password=user.password, 
            role_id=user.role_id
        ).returning(ORMUser.id, ORMUser.username, ORMUser.role_id)
        result = await self.session.execute(stmt)
        await self.session.commit()
        row = result.fetchone()
        if row:
            return User(id=row.id, username=row.username, password=user.password, role_id=row.role_id)
        return None

    async def delete_user(self, user_id: int) -> None:
        stmt = delete(ORMUser).where(ORMUser.id == user_id)
        result = await self.session.execute(stmt)
        await self.session.commit()
        if result.rowcount == 0:
            raise ValueError(f"User with id {user_id} not found")
