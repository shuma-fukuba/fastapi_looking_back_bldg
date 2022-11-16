from typing import Optional
from pydantic import BaseModel
from uuid import UUID

from .posse_year import PosseYear


class UserBase(BaseModel):
    uuid: UUID
    username: str
    university: str
    university_entrance_year: int
    expected_university_graduation_year: int
    github_username: Optional[str]
    github_repository: Optional[str]

    class Config:
        orm_mode = True


class User(UserBase):
    posse_year: PosseYear

    class Config:
        orm_mode = True
