from datetime import date, datetime
from uuid import UUID
from pydantic import BaseModel


class PosseYearBase(BaseModel):
    uuid: UUID
    year: float
    entrance_date: date


class PosseYear(PosseYearBase):
    updated_at: datetime

    class Config:
        orm_mode = True
