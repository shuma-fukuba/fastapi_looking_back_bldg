from sqlalchemy import and_
from sqlalchemy.orm import Session
from sqlalchemy.exc import StatementError
from fastapi import HTTPException

from models import LearningTime, LookingBack, User, Week, InputCurriculum, OutputCurriculum, Week
from utils.logger import get_logger
from starlette.status import HTTP_400_BAD_REQUEST
from .domains.Week import Week as WeekDomain


logger = get_logger(__name__)


def read_home(db: Session,
              user_id: str):
    try:
        user: User = db.query(User).get(user_id)
    except StatementError:
        pass

    if not user:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail='Invalid user id given.')

    week = WeekDomain.get_this_week(db=db,
                                    model=Week,
                                    entrance_date=user.posse_year.entrance_date)

    # input_curriculums = db.query(InputCurriculum).filter(
    #     InputCurriculum.week == week).all()

    # output_curriculums = db.query(OutputCurriculum).filter(
    #     OutputCurriculum.week == week
    # ).all()

    try:
        learning_time = db.query(LearningTime).filter(and_(
            LearningTime.user == user,
            LearningTime.week == week
        )).one_or_none()
    except StatementError:
        pass

    return learning_time

    # return output_curriculums 
