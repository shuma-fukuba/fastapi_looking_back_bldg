from sqlalchemy.orm import Session
from sqlalchemy.exc import StatementError
from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from models import InputCurriculum, User, UsersInputCurriculums

from utils.logger import get_logger


logger = get_logger(__name__)


def get_input_curriculums(db: Session,
                          user_id: str,
                          model: InputCurriculum,
                          user_model: User):
    user = _get_user(db=db, model=user_model, user_id=user_id)
    try:
        items = db.query(model, UsersInputCurriculums)\
            .join(UsersInputCurriculums,
                  model.uuid ==
                  UsersInputCurriculums.input_curriculum_id)\
            .filter(UsersInputCurriculums.users == user)\
            .all()
    # except Exception:
    #     raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
    #                         detail='Unrecognized id format.')
    except StatementError:
        pass
    if not items:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Record not found.')
    return items


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
