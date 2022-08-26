from typing import List
from pydantic import BaseModel
from schemas import HomeLookingBack, HomeLearningTime, Curriculum


class ResponseHomeSchema(BaseModel):
    user_id: str
    learning_time: HomeLearningTime = None
    looking_back: HomeLookingBack = None
    input_curriculums: List[Curriculum] = None
    output_curriculums: List[Curriculum] = None

    class Config:
        orm_mode = True
