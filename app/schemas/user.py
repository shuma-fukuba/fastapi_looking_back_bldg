from typing import Optional
from pydantic import BaseModel
from uuid import UUID


class UserBase(BaseModel):
    uuid: UUID
    username: str
    university: str
    university_entrance_year: str
    expected_university_graduation_year: str
    line_id: Optional[str]
