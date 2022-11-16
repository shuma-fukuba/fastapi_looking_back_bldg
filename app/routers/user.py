from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from cruds import user as crud
from database import get_db
from models import User
import schemas

router = APIRouter()


@router.get('/', response_model=List[schemas.User])
async def read_users(db: Session = Depends(get_db)):  # current userは認証してる
    return crud.read_users(db=db, model=User)


@router.get('/{user_id}', response_model=schemas.User)
async def read_user(user_id: str, db: Session = Depends(get_db)):
    return crud.read_user(user_id=user_id,
                          db=db,
                          model=User)
