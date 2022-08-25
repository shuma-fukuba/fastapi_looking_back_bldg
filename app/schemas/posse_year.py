from datetime import date
from uuid import UUID
from pydantic import BaseModel


class PosseYearBase(BaseModel):
    uuid: UUID
    year: float
    entrance_date: date


class PosseYear(PosseYearBase):
    class Config:
        orm_mode = True
