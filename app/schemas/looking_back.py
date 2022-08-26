from uuid import UUID
from pydantic import BaseModel

from .week import WeekBase
from .user import UserBase


class LookingBackBase(BaseModel):
    uuid: UUID
    good_point: str
    why_it_worked: str
    should_continue: str
    bad_point: str
    why_it_didnt_worked: str
    should_stop: str
    improve_point: str


class LookingBack(LookingBackBase):
    week: WeekBase
    user: UserBase

    class Config:
        orm_mode = True


class HomeLookingBack(LookingBackBase):
    class Config:
        orm_mode = True


class LookingBackCreate(BaseModel):
    good_point: str
    why_it_worked: str
    should_continue: str
    bad_point: str
    why_it_didnt_worked: str
    should_stop: str
    improve_point: str
    week: int
