from typing import Optional

from pydantic import BaseModel, Field, validator


class MeetingRoomCreate(BaseModel):
    name: str = Field(..., max_lenght=100)
    description: Optional[str]


    @validator('name')
    def empty_name(cls, value: str):
        if value is not None:
            return value
        raise ValueError('name must not empty')
