from pydantic import BaseModel
from uuid import UUID


class LearningTimeBase(BaseModel):
    uuid: UUID
    learning_time: int
    created_at: str
    updated_at: str


class CreateLearningTimeSchema(BaseModel):
    week: int
    learning_time: int


class ResponseLearningTimeSchema(LearningTimeBase):
    user_id: UUID
    week_id: UUID
