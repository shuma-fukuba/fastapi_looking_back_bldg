from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from cruds import user as user_crud
from database import get_db
from models import User
import schemas

router = APIRouter()


@router.get('/', response_model=List[schemas.User])
async def read_users(db: Session = Depends(get_db)):  # current userは認証してる
    return user_crud.read_users(db=db, model=User)
