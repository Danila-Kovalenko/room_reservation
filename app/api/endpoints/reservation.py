from fastapi import APIRouter

from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.reservation import ReservationCreate
from app.api.validators import check_meeting_room_exists

router = APIRouter()


@router.post('/')
async def create_reservation(reservation: ReservationCreate,
                             session: AsyncSession, ):
    await check_meeting_room_exists

