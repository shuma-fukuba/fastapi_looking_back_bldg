from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from cruds import user as crud
from database import get_db
from models import User
from modules.auth.auth import get_current_active_user
import schemas

router = APIRouter()


@router.get('/me', response_model=schemas.User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.get('/', response_model=List[schemas.User])
async def read_users(db: Session = Depends(get_db),
                     current_user: User = Depends(get_current_active_user)):
    return crud.read_users(db=db, model=User)
