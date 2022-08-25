from pydantic import BaseModel
from uuid import UUID

from .week import WeekBase
from .user import UserBase


class LearningTimeBase(BaseModel):
    uuid: UUID
    learning_time: int


class LearningTime(LearningTimeBase):
    # week: WeekBase = None
    # user: UserBase = None

    class Config:
        orm_mode = True


class CreateLearningTimeSchema(BaseModel):
    week: int
    learning_time: int


class ResponseLearningTimeSchema(LearningTimeBase):
    user_id: UUID
    week_id: UUID


class UpdateLearningTimeSchema(BaseModel):
    learning_time: int
