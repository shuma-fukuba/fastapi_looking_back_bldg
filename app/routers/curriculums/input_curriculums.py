from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

from models import InputCurriculum, User
from cruds.curriculums import input_curriculums as crud


router = APIRouter()


@router.get('/{user_id}')
async def get_input_curriculums(user_id,
                                db: Session = Depends(get_db)):
    return crud.get_input_curriculums(db=db,
                                      user_id=user_id,
                                      model=InputCurriculum,
                                      user_model=User)
