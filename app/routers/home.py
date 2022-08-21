from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from cruds import home as crud
# from schemas import ResponseHomeSchema


router = APIRouter()


@router.get('/')
async def home(user_id,
               db: Session = Depends(get_db)):
    return crud.read_home(db=db,
                          user_id=user_id)
