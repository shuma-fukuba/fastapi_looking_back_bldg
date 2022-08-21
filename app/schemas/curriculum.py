from xmlrpc.client import boolean
from pydantic import BaseModel
from uuid import UUID


class CurriculumBase(BaseModel):
    uuid: UUID
    curriculum_name: str


class ResponseCurriculumSchema(CurriculumBase):
    is_done: bool = False
