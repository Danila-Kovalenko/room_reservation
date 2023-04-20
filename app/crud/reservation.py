from datetime import datetime as dt
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.reservation import Reservation


class CRUDReservation(CRUDBase):

    async def get_reservations_at_the_same_time(self,
                                                meetingroom_id: int,
                                                from_reserve: dt,
                                                to_reserve: dt,
                                                session: AsyncSession,
                                                ) -> List[Reservation]:
        """Метод ищущий пересекающиеся объекты по времени с интервалом,
        указанном в запросе."""

        return []


reservation_crud = CRUDReservation(Reservation)
