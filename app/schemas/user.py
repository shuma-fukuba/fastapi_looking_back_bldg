from datetime import datetime
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


class User(UserBase):
    class Config:
        orm_mode = True


class ResponseUserSchema(UserBase):
    posse_year: PosseYear
    updated_at: datetime

    class Config:
        orm_mode = True
