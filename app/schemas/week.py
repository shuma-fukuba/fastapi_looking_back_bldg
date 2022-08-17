from pydantic import BaseModel
from uuid import UUID


class WeekBase(BaseModel):
    uuid: UUID
    week: int


class ResponseWeekSchema(WeekBase):
    pass
