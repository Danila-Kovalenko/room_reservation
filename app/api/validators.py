from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.meeting_room import meeting_room_crud
from app.crud.reservation import reservation_crud
from app.models.meeting_room import MeetingRoom


async def check_name_duplicate(room_name: str,
                               session: AsyncSession,) -> None:
    """Корутина, проверяющая уникальность полученного имени переговорки."""
    room_id = meeting_room_crud.get_room_id_by_name(room_name, session)
    if room_id is not None:
        raise HTTPException(
            status_code=422,
            detail='Переговорка с таким именем уже существует!',
        )

async def check_meeting_room_exists(meeting_room_id: int,
                                    session: AsyncSession) -> MeetingRoom:
    """Корутина, проверяющая наличие переговорки."""
    meeting_room = await meeting_room_crud.get(meeting_room_id, session)
    if meeting_room is None:
        raise HTTPException(status_code=404,
                            detail='Переговорка не найдена!')
    return meeting_room

async def check_reservation_intersections(**kwagrs) -> None:
    """Корутина, проверяющая свободен ли запрошенный интервал времени для переговорки."""
    reserv = await reservation_crud.get_reservations_at_the_same_time(**kwagrs)
    if reserv is not None:
        raise HTTPException(status_code=422,
                            detail=str(reserv))

async def check_reservation_before_edit(reservation_id:int, session: AsyncSession,):
    """Корутина, проверяющая существует ли запрошенный объект бронирования."""
    reservation = await reservation_crud.get(reservation_id, session)
    if not reservation:
        raise HTTPException(status_code=404,
                            detail='Бронь не найдена!')
    return reservation
