from pydantic import BaseModel
from uuid import UUID


class LearningTimeBase(BaseModel):
    uuid: UUID
    learning_time: int
