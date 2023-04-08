from typing import Optional

from pydantic import BaseModel, Field, validator


class MeetingRoomBase(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    description: Optional[str]



class MeetingRoomCreate(MeetingRoomBase):
    name: str = Field(..., max_length=100)

    @validator('name')
    def empty_name(cls, value: str):
        if value is not None:
            return value
        raise ValueError('name must not empty')


class MeetingRoomUpdate(MeetingRoomBase):
    pass


class MeetingRoomDB(MeetingRoomCreate):
    id: int

    class Config:
        orm_mode = True
