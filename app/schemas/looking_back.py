from pydantic import BaseModel

from .week import Week


class LookingBackBase(BaseModel):
    good_point: str
    why_it_worked: str
    should_continue: str
    bad_point: str
    why_it_didnt_worked: str
    should_stop: str
    improve_point: str


class LookingBack(LookingBackBase):
    pass


class LookingBackCreate(LookingBackBase):
    week: int


class ResponseLookingBack(LookingBackBase):
    uuid: str
    user_id: str
    week_id: str
    week: Week
    # user: User
