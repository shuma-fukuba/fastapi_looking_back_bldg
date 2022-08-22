from sqlalchemy import and_
from sqlalchemy.orm import Session
from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from models import OutputCurriculum, User, UsersOutputCurriculums

from utils.logger import get_logger


logger = get_logger(__name__)


def get_output_curriculums(db: Session,
                           user_id: str,
                           model: OutputCurriculum,
                           user_model: User):
    user = _get_user(db=db, model=user_model, user_id=user_id)
    try:
        items = db.query(model, UsersOutputCurriculums)\
            .join(UsersOutputCurriculums,
                  model.uuid ==
                  UsersOutputCurriculums.output_curriculum_id)\
            .filter(UsersOutputCurriculums.users == user)\
            .all()
    except Exception:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail='Unrecognized id format.')
    if not items:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Record not found.')
    return items


def get_output_curriculum(db: Session,
                          user_id: str,
                          curriculum_id: str,
                          model: OutputCurriculum,
                          association_model: UsersOutputCurriculums,
                          user_model: User):
    user = _get_user(db=db, model=user_model, user_id=user_id)
    try:
        item: OutputCurriculum = db.query(model, association_model)\
            .join(association_model, model.uuid == association_model.output_curriculum_id)\
            .filter(and_(model.uuid == curriculum_id,
                         association_model.users == user)).one_or_none()
    except Exception:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail='Unrecognized id format.')
    if not item:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Record not found.')
    return item


def udpate_curriculum_done(db: Session,
                           user_id: str,
                           curriculum_id: str,
                           done: bool,
                           model: UsersOutputCurriculums):
    try:
        item: UsersOutputCurriculums = db.query(model).filter(and_(
            model.user_id == user_id,
            model.output_curriculum_id == curriculum_id
        )).one_or_none()
    except Exception:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail='Unrecognized id format.')
    if not item:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Record not found.')
    item.done = done
    db.commit()
    return (user_id, curriculum_id)


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
