from sqlalchemy.orm import Session
from sqlalchemy.exc import StatementError
from fastapi import HTTPException
from starlette.status import HTTP_404_NOT_FOUND

from utils.logger import get_logger
from models import User


logger = get_logger(__name__)


def read_users(db: Session, model: User):
    try:
        users = db.query(model).all()
    except StatementError:
        pass

    if not users:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Record not found.')
    return users
