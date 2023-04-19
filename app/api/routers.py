from fastapi import APIRouter
from .endpoints.reservation import router as reservation_router
from .endpoints.meeting_room import router as meeting_room_router


main_router = APIRouter()
main_router.include_router(meeting_room_router)
main_router.include_router(reservation_router)
