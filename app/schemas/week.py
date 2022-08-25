from pydantic import BaseModel
from uuid import UUID


class WeekBase(BaseModel):
    uuid: UUID
    week: int

    class Config:
        orm_mode = True


class Week(WeekBase):
    class Config:
        orm_mode = True
