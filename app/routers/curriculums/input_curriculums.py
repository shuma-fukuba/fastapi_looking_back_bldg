from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

from models import InputCurriculum, User, UsersInputCurriculums
from cruds.curriculums import input_curriculums as crud


router = APIRouter()


@router.get('/{user_id}')
async def get_input_curriculums(user_id,
                                db: Session = Depends(get_db)):
    return crud.get_input_curriculums(db=db,
                                      user_id=user_id,
                                      model=InputCurriculum,
                                      user_model=User)


@router.get('/{user_id}/{curriculum_id}')
async def get_input_curriculum(user_id,
                               curriculum_id,
                               db: Session = Depends(get_db)):
    return crud.get_input_curriculum(db=db,
                                     user_id=user_id,
                                     curriculum_id=curriculum_id,
                                     model=InputCurriculum,
                                     association_model=UsersInputCurriculums,
                                     user_model=User)
