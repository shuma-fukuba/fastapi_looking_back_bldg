from typing import List
from pydantic import BaseModel

from schemas.user import UserBase
from schemas.curriculum import CurriculumBase


class UsersInputCurriculumBase(BaseModel):
    done: bool


class UsersInputCurriculum(UsersInputCurriculumBase):
    users: List[UserBase] = None
    input_curriculums: List[CurriculumBase] = None

    class Config:
        orm_mode = True
