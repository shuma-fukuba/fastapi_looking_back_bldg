from sqlite3 import IntegrityError
from sqlalchemy import and_
from sqlalchemy.orm import Session
from sqlalchemy.exc import StatementError
from fastapi import HTTPException

from models import LearningTime, User, Week
from utils.logger import get_logger
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from .domains.Week import Week as WeekDomain
from schemas import CreateLearningTimeSchema


logger = get_logger(__name__)


# TODO add week num
def read_learning_times(db: Session, user_id: str, model: LearningTime):
    user = _get_user(db=db, model=User, user_id=user_id)

    try:
        learning_times = db.query(model).filter(model.user == user).all()
    except StatementError:
        pass

    return learning_times


def read_learning_time_in_this_week(db: Session,
                                    model: LearningTime,
                                    user_model: User,
                                    user_id: str):
    user = _get_user(db=db, model=user_model, user_id=user_id)
    entrance_date = user.posse_year.entrance_date

    this_week_id = WeekDomain.get_this_week_id(db=db,
                                               model=Week,
                                               entrance_date=entrance_date)

    try:
        item = db.query(model).filter(
            model.week_id == this_week_id
        ).one_or_none()
    except StatementError:
        pass

    if not item:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Record not found.')
    return item


def read_learning_time(db: Session,
                       model: LearningTime,
                       user_model: User,
                       user_id: str,
                       week_num: int):
    user = _get_user(db=db, model=user_model, user_id=user_id)
    try:
        week = db.query(Week).filter(Week.week == week_num).one_or_none()
    except Exception:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail='Unrecognized week num format.')
    if not week:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Week not found.')

    try:
        item = db.query(model).filter(and_(
            model.user == user,
            model.week == week
        )).one_or_none()
    except Exception:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail='Unrecognized id format.')

    if not item:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Record not found.')
    return item


def create_learning_time(db: Session,
                         user_id: str,
                         user_model: User,
                         params: CreateLearningTimeSchema):
    learning_time = params.learning_time
    week = params.week

    user = _get_user(db=db, model=user_model, user_id=user_id)

    try:
        db_week = db.query(Week).filter(Week.week == week).one_or_none()
    except StatementError:
        pass

    if not db_week:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail='Invalid week given.')

    try:
        db_item: LearningTime = LearningTime(learning_time=learning_time)
        db_item.user = user
        db_item.week = db_week
        db.add(db_item)
        db.commit()
    except IntegrityError:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail='Validation failed.')

    db.refresh(db_item)
    return db_item


def update_learning_time(db: Session,
                         user_id: str,
                         learning_time_id: str,
                         learning_time: int,
                         model: LearningTime,
                         user_model: User):
    user = _get_user(db=db, model=user_model, user_id=user_id)

    try:
        item = db.query(model).get(learning_time_id)
    except Exception:  # expect invalid id given
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail='Unrecognized id format.')
    if not item:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Record not found.')
    if item.user != user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Record not found.')

    if learning_time:
        item.learning_time = learning_time

    db.commit()
    return learning_time_id


def delete_learning_time(db: Session,
                         user_id: str,
                         learning_time_id: str,
                         model: LearningTime,
                         user_model: User):
    user = _get_user(db=db, model=user_model, user_id=user_id)

    try:
        item = db.query(model).get(learning_time_id)
    except Exception:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail='Unrecognized id format.')
    if not item:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Record not found.')
    if item.user != user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Record not found.')

    db.delete(item)
    db.commit()
    return True


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
