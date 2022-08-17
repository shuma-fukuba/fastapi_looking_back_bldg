from pydantic import BaseModel
from uuid import UUID


class LookinBackBase(BaseModel):
    uuid: UUID
    good_point: str
    why_it_worked: str
    should_continue: str
    bad_point: str
    why_it_didnt_worked: str
    should_stop: str
    improve_point: str
