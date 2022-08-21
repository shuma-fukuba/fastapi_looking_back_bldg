from sqlalchemy import and_
from sqlalchemy.orm import Session
from sqlalchemy.exc import StatementError
from fastapi import HTTPException

from models import LearningTime, LookingBack, User, Week, InputCurriculum, OutputCurriculum, UsersInputCurriculums
from models.associations.users_output_curriculums import UsersOutputCurriculums
from utils.logger import get_logger
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from .domains.Week import Week as WeekDomain


logger = get_logger(__name__)


def read_home(db: Session,
              user_id: str):
    user = _get_user(db=db, model=User, user_id=user_id)
    week = WeekDomain.get_this_week(db=db,
                                    model=Week,
                                    entrance_date=user.posse_year.entrance_date)

    input_curriculums = db.query(InputCurriculum.curriculum_name,
                                 UsersInputCurriculums.done)\
        .join(UsersInputCurriculums,
              InputCurriculum.uuid == UsersInputCurriculums.input_curriculum_id)\
        .filter(and_(
            InputCurriculum.week == week,
            UsersInputCurriculums.users == user))\
        .all()

    output_curriculums = db.query(OutputCurriculum.curriculum_name,
                                  UsersOutputCurriculums.done)\
        .join(UsersOutputCurriculums,
              OutputCurriculum.uuid == UsersOutputCurriculums.output_curriculum_id)\
        .filter(and_(
            OutputCurriculum.week == week,
            UsersOutputCurriculums.users == user))\
        .all()

    try:
        learning_time = db.query(LearningTime)\
            .filter(and_(
                    LearningTime.user == user,
                    LearningTime.week == week
                    )).one_or_none()
    except StatementError:
        pass

    looking_back = db.query(LookingBack)\
        .filter(LookingBack.user == user,
                LookingBack.week == week)\
        .one_or_none()

    return {
        'input_curriculums': input_curriculums,
        'output_curriculums': output_curriculums,
        'learning_time': learning_time.learning_time,
        'looking_back': looking_back
    }


def _get_user(db: Session,
              model: User,
              user_id: str):
    try:
        user = db.query(model).get(user_id)
    except Exception:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail='Unrecognized id format.')
    if not user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Record not found.')
    return user
