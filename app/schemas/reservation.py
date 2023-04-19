from datetime import datetime as dt

from pydantic import BaseModel, Field, root_validator, validator


class ReservationBase(BaseModel):
    """Базовый класс схемы для бронирования."""
    from_reserve: dt
    to_reserve: dt


class ReservationUpdate(ReservationBase):

    @validator('from_reserve')
    def check_from_reserve_later_than_now(cls, value):
        if dt.now() >= value:
            raise ValueError('Время начала бронирования '
                'не может быть меньше текущего времени')
        return value

    @root_validator(skip_on_failure=True)
    def check_from_reserve_before_to_reserve(cls, value):
        if value['from_reserve'] >= value ['to_reserve']:
            raise ValueError('Время начала бронирования '
                'не может быть больше времени окончания')
        return value


class ReservationCreate(ReservationBase):
    meetingroom_id: int


class ReservationDB(ReservationBase):
    meetingroom_id: int
    id: int


    class Config:
        orm_mode = True
