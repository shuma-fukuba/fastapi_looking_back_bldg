from pydantic import BaseModel
from schemas import LookingBack, LearningTime


class ResponseHomeSchema(BaseModel):
    user_id: str
    learning_time: LearningTime = None
    looking_back: LookingBack = None
    # input_curriculums: List[ResponseCurriculumSchema] = None
    # output_curriculums: List[ResponseCurriculumSchema] = None

    class Config:
        orm_mode = True
