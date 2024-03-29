from typing import Optional
from pydantic import BaseModel
from uuid import UUID

from .posse_year import PosseYear


class UserBase(BaseModel):
    uuid: UUID
    username: str
    email: str
    hashed_password: str
    university: str
    university_entrance_year: int
    expected_university_graduation_year: int
    line_id: Optional[str]
    cognito_user_id: Optional[str]
    github_username: Optional[str]
    github_repository: Optional[str]
    github_access_token: Optional[str]

    class Config:
        orm_mode = True


class User(UserBase):
    disabled: bool = False
    posse_year: PosseYear

    class Config:
        orm_mode = True
