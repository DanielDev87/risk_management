from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import insert, update, delete
from sqlalchemy.exc import IntegrityError
from typing import List, Optional
from infrastructure.orm.models import Event
from domain.entities.Event import Event as EventEntity


class EventRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_event(self, event: EventEntity) -> EventEntity:
        stmt = insert(Event).values(
            risk_type_id=event.risk_type_id,
            factor=event.factor,
            description=event.description,
            probability_id=event.probability_id,
            impact_id=event.impact_id
        ).returning(
            Event.id,
            Event.risk_type_id,
            Event.factor,
            Event.description,
            Event.probability_id,
            Event.impact_id
        )

        try:
            result = await self.session.execute(stmt)
            await self.session.commit()
            row = result.fetchone()
            if row:
                return EventEntity(
                    id=row.id,
                    risk_type_id=row.risk_type_id,
                    factor=row.factor,
                    description=row.description,
                    probability_id=row.probability_id,
                    impact_id=row.impact_id
                )
        except IntegrityError as e:
            await self.session.rollback()
            raise ValueError("Event already exists") from e

    async def get_event(self, event_id: int) -> Optional[EventEntity]:
        stmt = select(Event).where(Event.id == event_id)
        result = await self.session.execute(stmt)
        event = result.scalar_one_or_none()
        if event:
            return EventEntity(
                id=event.id,
                risk_type_id=event.risk_type_id,
                factor=event.factor,
                description=event.description,
                probability_id=event.probability_id,
                impact_id=event.impact_id
            )
        return None

    async def get_all_events(self) -> List[EventEntity]:
        stmt = select(Event)
        result = await self.session.execute(stmt)
        events = result.scalars().all()
        return [
            EventEntity(
                id=e.id,
                risk_type_id=e.risk_type_id,
                factor=e.factor,
                description=e.description,
                probability_id=e.probability_id,
                impact_id=e.impact_id
            ) for e in events
        ]

    async def update_event(self, event_id: int, event: EventEntity) -> Optional[EventEntity]:
        stmt = update(Event).where(Event.id == event_id).values(
            risk_type_id=event.risk_type_id,
            factor=event.factor,
            description=event.description,
            probability_id=event.probability_id,
            impact_id=event.impact_id
        ).returning(
            Event.id,
            Event.risk_type_id,
            Event.factor,
            Event.description,
            Event.probability_id,
            Event.impact_id
        )

        result = await self.session.execute(stmt)
        await self.session.commit()
        row = result.fetchone()
        if row:
            return EventEntity(
                id=row.id,
                risk_type_id=row.risk_type_id,
                factor=row.factor,
                description=row.description,
                probability_id=row.probability_id,
                impact_id=row.impact_id
            )
        return None

    async def delete_event(self, event_id: int) -> None:
        stmt = delete(Event).where(Event.id == event_id)
        result = await self.session.execute(stmt)
        await self.session.commit()
        if result.rowcount == 0:
            raise ValueError(f"Event with id {event_id} not found")
