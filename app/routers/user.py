from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from cruds import user as crud
from database import get_db
from models import User

router = APIRouter()


@router.get('/')
async def read_users(db: Session = Depends(get_db)):
    return crud.read_users(db=db, model=User)
