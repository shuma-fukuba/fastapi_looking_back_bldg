from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

from models import LearningTime, User
from cruds import learning_time as crud
from schemas import CreateLearningTimeSchema, ResponseLearningTimeSchema

router = APIRouter()


@router.get('/{user_id}')
async def read_learning_times(user_id,
                              db: Session = Depends(get_db)):
    return crud.read_learning_times(db=db,
                                    user_id=user_id,
                                    model=LearningTime)


@router.get('/{user_id}/this_week')
async def read_learning_time_in_this_week(user_id,
                                          db: Session = Depends(get_db)):
    return crud.read_learning_time(db=db,
                                   model=LearningTime,
                                   user_model=User,
                                   user_id=user_id)


@router.post('/{user_id}')
async def create_learning_time(user_id: str,
                               params: CreateLearningTimeSchema,
                               db: Session = Depends(get_db)):
    return crud.create_learning_time(db=db,
                                     user_model=User,
                                     user_id=user_id,
                                     params=params)
