from pydantic import BaseModel
from uuid import UUID
# from .week import WeekBase
# from .user import UserBase


class CurriculumBase(BaseModel):
    uuid: UUID
    curriculum_name: str


class Curriculum(CurriculumBase):
    class Config:
        orm_mode = True


class UpdateCurriculumSchema(BaseModel):
    done: bool = False


class ResponseCurriculumSchema(CurriculumBase):
    pass
