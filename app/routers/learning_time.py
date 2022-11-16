from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

from models import LearningTime, User
from cruds import learning_time as crud
import schemas

router = APIRouter()


@router.get('/{user_id}', response_model=List[schemas.LearningTime])
async def read_learning_times(user_id,
                              db: Session = Depends(get_db)):
    return crud.read_learning_times(db=db,
                                    user_id=user_id,
                                    model=LearningTime)


@router.get('/{user_id}/this_week', response_model=schemas.LearningTime)
async def read_learning_time_in_this_week(user_id,
                                          db: Session = Depends(get_db)):
    return crud.read_learning_time_in_this_week(db=db,
                                                model=LearningTime,
                                                user_model=User,
                                                user_id=user_id)


@router.get('/{user_id}/{week}', response_model=schemas.LearningTime)
async def read_learning_time(user_id,
                             week,
                             db: Session = Depends(get_db)):
    return crud.read_learning_time(db=db,
                                   user_id=user_id,
                                   week_num=week,
                                   model=LearningTime,
                                   user_model=User)
