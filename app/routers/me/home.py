from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from cruds import home as crud
from modules.auth.auth import get_current_active_user
from models import User


router = APIRouter()


@router.get('/')
async def home(current_user: User = Depends(get_current_active_user),
               db: Session = Depends(get_db)):
    user_id = current_user.uuid
    return crud.read_home(db=db,
                          user_id=user_id)
