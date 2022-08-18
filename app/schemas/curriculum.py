from pydantic import BaseModel
from uuid import UUID


class CurriculumBase(BaseModel):
    uuid: UUID
    curriculum_name: str
