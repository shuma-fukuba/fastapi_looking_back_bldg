from typing import List
from pydantic import BaseModel

from schemas.user import UserBase
from schemas.curriculum import CurriculumBase


class UsersOutputCurriculumBase(BaseModel):
    done: bool


class UsersOutputCurriculum(UsersOutputCurriculumBase):
    users: List[UserBase] = None
    output_curriculums: List[CurriculumBase] = None

    class Config:
        orm_mode = True
