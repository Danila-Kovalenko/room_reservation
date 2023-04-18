from datetime import datetime as dt

from pydantic import BaseModel, Field, validator


class ReservationBase(BaseModel):
    """Базовый класс схемы для бронирования."""
    from_reserve: dt
    to_reserve: dt


class ReservationCreate(ReservationBase):
    meetingroom_id: int


class ReservationUpdate(ReservationBase):
    pass


class ReservationDB(ReservationBase):
    meetingroom_id: int
    id: int


    class Config:
        orm_mode = True
