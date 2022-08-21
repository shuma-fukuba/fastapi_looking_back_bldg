from sqlite3 import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy.exc import StatementError
from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
import schemas

from utils.logger import get_logger
from models import LookingBack, User, Week
from ..domains.Week import Week as WeekDomain

logger = get_logger(__name__)


def read_looking_back(db: Session,
                      model: LookingBack,
                      user_model: User,
                      user_id: str):
    user = _get_user(db=db,
                     model=user_model,
                     user_id=user_id)

    entrance_date = user.posse_year.entrance_date

    this_week_id = WeekDomain.get_this_week_id(
        db=db,
        model=Week,
        entrance_date=entrance_date)

    try:
        item = db.query(model).filter(
            model.week_id == this_week_id).one_or_none()
    except StatementError:
        pass

    return item


def read_looking_backs(db: Session,
                       model: LookingBack,
                       user_model: User,
                       user_id: str
                       ):
    user = _get_user(db=db,
                     model=user_model,
                     user_id=user_id)

    try:
        items = db.query(model).filter(model.user == user).all()
    except StatementError:
        pass

    if not items:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Record not found.')

    return items


def create_looking_back(params: schemas.LookingBackCreate,
                        user_id,
                        model: LookingBack,
                        db: Session):
    try:
        db_item = model(
            good_point=params.good_point,
            why_it_worked=params.why_it_worked,
            should_continue=params.should_continue,
            bad_point=params.bad_point,
            why_it_didnt_worked=params.why_it_didnt_worked,
            should_stop=params.should_stop,
            improve_point=params.improve_point,
            user_id=user_id
        )
        # db_item.week = params.week
        try:
            week = db.query(Week).filter(
                Week.week == params.week).one()
        except StatementError:
            pass

        if not week:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                                detail='Invalid week given.')
        db_item.week = week
        db.add(db_item)
        db.commit()

    except IntegrityError:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail='Validation failed.')

    db.refresh(db_item)
    return db_item


def update_looking_back(db: Session,
                        model: LookingBack,
                        user_model: User,
                        user_id: str,
                        looking_back_id: str,
                        params: schemas.LookingBack):
    user = _get_user(db=db,
                     model=user_model,
                     user_id=user_id)

    # TODO なぜかnot found
    try:
        item = db.query(model).get(looking_back_id)
    except Exception:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail='Unrecognized id format.')
    if not item:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Record not found.')
    if item.user != user:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Record not found.')

    item.good_point = params.good_point
    item.why_it_worked = params.why_it_worked
    item.should_continue = params.should_continue
    item.bad_point = params.bad_point
    item.why_it_didnt_worked = params.why_it_didnt_worked
    item.should_stop = params.should_stop
    item.improve_point = params.improve_point

    db.commit()
    return looking_back_id


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
