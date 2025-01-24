from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import insert, update, delete
from typing import List, Optional
from domain.entities.Channel import Channel
from infrastructure.orm.models import Channel as ORMChannel

class ChannelRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_channel(self, channel: Channel) -> Channel:
        stmt = insert(ORMChannel).values(description=channel.description).returning(ORMChannel.id, ORMChannel.description)
        result = await self.session.execute(stmt)
        await self.session.commit()
        row = result.fetchone()
        if row:
            return Channel(id=row.id, description=row.description)

    async def get_channel(self, channel_id: int) -> Optional[Channel]:
        stmt = select(ORMChannel).where(ORMChannel.id == channel_id)
        result = await self.session.execute(stmt)
        orm_channel = result.scalar_one_or_none()
        if orm_channel:
            return Channel(id=orm_channel.id, description=orm_channel.description)
        return None

    async def get_all_channels(self) -> List[Channel]:
        stmt = select(ORMChannel)
        result = await self.session.execute(stmt)
        orm_channels = result.scalars().all()
        return [Channel(id=c.id, description=c.description) for c in orm_channels]

    async def update_channel(self, channel_id: int, channel: Channel) -> Optional[Channel]:
        stmt = update(ORMChannel).where(ORMChannel.id == channel_id).values(description=channel.description).returning(ORMChannel.id, ORMChannel.description)
        result = await self.session.execute(stmt)
        await self.session.commit()
        row = result.fetchone()
        if row:
            return Channel(id=row.id, description=row.description)
        return None

    async def delete_channel(self, channel_id: int) -> None:
        stmt = delete(ORMChannel).where(ORMChannel.id == channel_id)
        result = await self.session.execute(stmt)
        await self.session.commit()
        if result.rowcount == 0:
            raise ValueError(f"Channel with id {channel_id} not found")
