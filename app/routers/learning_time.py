from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

from models import LearningTime, User
from cruds import learning_time as crud
from schemas import CreateLearningTimeSchema, UpdateLearningTimeSchema

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
    return crud.read_learning_time_in_this_week(db=db,
                                                model=LearningTime,
                                                user_model=User,
                                                user_id=user_id)


@router.get('/{user_id}/{week}')
async def read_learning_time(user_id,
                             week,
                             db: Session = Depends(get_db)):
    return crud.read_learning_time(db=db,
                                   user_id=user_id,
                                   week_num=week,
                                   model=LearningTime,
                                   user_model=User)


@router.post('/{user_id}')
async def create_learning_time(user_id: str,
                               params: CreateLearningTimeSchema,
                               db: Session = Depends(get_db)):
    return crud.create_learning_time(db=db,
                                     user_model=User,
                                     user_id=user_id,
                                     params=params)


@router.put('/{user_id}/{learning_time_id}')
async def update_learning_time(user_id: str,
                               learning_time_id: str,
                               params: UpdateLearningTimeSchema,
                               db: Session = Depends(get_db)):
    learning_time = params.learning_time
    return crud.update_learning_time(db=db,
                                     user_id=user_id,
                                     learning_time_id=learning_time_id,
                                     model=LearningTime,
                                     user_model=User,
                                     learning_time=learning_time)


@router.delete('/{user_id}/{learning_time_id}')
async def delete_learning_time(user_id,
                               learning_time_id,
                               db: Session = Depends(get_db)):
    return crud.delete_learning_time(db=db,
                                     user_id=user_id,
                                     learning_time_id=learning_time_id,
                                     user_model=User,
                                     model=LearningTime)
