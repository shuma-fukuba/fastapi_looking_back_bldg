from optparse import Option
from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class UserBase(BaseModel):
    uuid: UUID
    username: str
    university: str
    university_entrance_year: str
    expected_university_graduation_year: str
    posse_year_id: str
    line_id: Optional[str]
    cognito_user_id: Optional[str]
    github_username: Optional[str]
    github_repository: Optional[str]
    github_access_token: Optional[str]

