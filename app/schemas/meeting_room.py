from typing import Optional

from pydantic import BaseModel, Field, validator


class MeetingRoomBase(BaseModel):
    name: Optional[str] = Field(None, min_lenght=1, max_lenght=100)
    description: Optional[str]


class MeetingRoomCreate(MeetingRoomBase):
    name: str = Field(..., min_lenght=1, max_lenght=100)


    @validator('name')
    def empty_name(cls, value: str):
        if value is not None:
            return value
        raise ValueError('name must not empty')


class MeetingRoomDB(BaseModel):
    id: int
