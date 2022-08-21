from typing import Optional, List
from pydantic import BaseModel
from schemas import ResponseCurriculumSchema, LookingBack


class ResponseHomeSchema(BaseModel):
    user_id: str
    learning_time: int
    looking_backs: Optional[LookingBack] = None
    input_curriculums: Optional[List[ResponseCurriculumSchema]] = None
    output_curriculums: Optional[List[ResponseCurriculumSchema]] = None
