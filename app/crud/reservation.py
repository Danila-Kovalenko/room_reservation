from datetime import datetime as dt
from typing import List, Optional

from sqlalchemy import and_, between, func, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Reservation, User


class CRUDReservation(CRUDBase):

    async def get_reservations_at_the_same_time(self,
            # Добавляем звёздочку, чтобы обозначить, что все дальнейшие параметры
            # должны передаваться по ключу. Это позволит располагать
            # параметры со значением по умолчанию перед параметрами без таких значений.
                                                *,
                                                meetingroom_id: int,
                                                from_reserve: dt,
                                                to_reserve: dt,
                                                reservation_id: Optional[int] = None,
                                                session: AsyncSession,
                                                ) -> List[Reservation]:
        """Метод, ищущий пересекающиеся объекты по времени с интервалом,
        указанном в запросе."""
        # Выносим уже существующий запрос в отдельное выражение.
        select_stmt = select(Reservation).where(
            Reservation.meetingroom_id == meetingroom_id,
            and_(
                from_reserve <= Reservation.to_reserve,
                to_reserve >= Reservation.from_reserve
            )
        )
        # Если передан id бронирования...
        if reservation_id is not None:
            # ... то к выражению нужно добавить новое условие.
            select_stmt = select_stmt.where(
                # id искомых объектов не равны id обновляемого объекта.
                Reservation.id != reservation_id
            )
        # Выполняем запрос.
        reservations = await session.execute(select_stmt)
        reservations = reservations.scalars().all()
        return reservations

    async def get_future_reservations_for_room(self,
                                               room_id: int,
                                               session: AsyncSession):
        """Метод, ищущий объекты, период бронирования которых ещё не истёк."""
        reservations  = await session.execute(select(Reservation)).where(
            Reservation.meetingroom_id == room_id,
            Reservation.to_reserve >= dt.now())
        return reservations.scalars().all()

    async def get_by_user(
            self, session: AsyncSession, user: User
    ):
        reservations = await session.execute(
            select(Reservation).where(
                Reservation.user_id == user.id
            )
        )
        return reservations.scalars().all()

    async def get_count_res_at_the_same_time(self,
                                             from_reserve: dt,
                                             to_reserve: dt,
                                             session: AsyncSession,
                                             ):
        """Метод сообрает данные о том, сколько раз за указанный период
        была забронирована каждая переговорка."""
        reservations = await session.execute(
            # Получаем количество бронирований переговорок за период
            select([Reservation.meetingroom_id,
                    func.count(Reservation.meetingroom_id)]).where(
                Reservation.from_reserve >= from_reserve,
                Reservation.to_reserve <= to_reserve
            ).group_by(Reservation.meetingroom_id))
        reservations = reservations.all()
        return reservations


reservation_crud = CRUDReservation(Reservation)
