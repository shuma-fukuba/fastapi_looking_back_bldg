from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

from models import LearningTime, User
from cruds import learning_time as crud
from modules.auth.auth import get_current_active_user
import schemas

router = APIRouter()


@router.get('/{user_id}', response_model=List[schemas.LearningTime])
async def read_learning_times(user_id,
                              current_user=Depends(get_current_active_user),
                              db: Session = Depends(get_db)):
    return crud.read_learning_times(db=db,
                                    user_id=user_id,
                                    model=LearningTime)


@router.get('/{user_id}/this_week', response_model=schemas.LearningTime)
async def read_learning_time_in_this_week(user_id,
                                          current_user=Depends(
                                              get_current_active_user),
                                          db: Session = Depends(get_db)):
    return crud.read_learning_time_in_this_week(db=db,
                                                model=LearningTime,
                                                user_model=User,
                                                user_id=user_id)


@router.get('/{user_id}/{week}', response_model=schemas.LearningTime)
async def read_learning_time(user_id,
                             week,
                             current_user=Depends(get_current_active_user),
                             db: Session = Depends(get_db)):
    return crud.read_learning_time(db=db,
                                   user_id=user_id,
                                   week_num=week,
                                   model=LearningTime,
                                   user_model=User)


@router.post('/', response_model=schemas.LearningTime)
async def create_learning_time(params: schemas.CreateLearningTimeSchema,
                               current_user=Depends(get_current_active_user),
                               db: Session = Depends(get_db)):
    user_id = current_user.uuid
    return crud.create_learning_time(db=db,
                                     user_model=User,
                                     user_id=user_id,
                                     params=params)


@router.put('/{learning_time_id}')
async def update_learning_time(learning_time_id: str,
                               params: schemas.UpdateLearningTimeSchema,
                               current_user=Depends(get_current_active_user),
                               db: Session = Depends(get_db)):
    learning_time = params.learning_time
    user_id = current_user.uuid
    return crud.update_learning_time(db=db,
                                     user_id=user_id,
                                     learning_time_id=learning_time_id,
                                     model=LearningTime,
                                     user_model=User,
                                     learning_time=learning_time)


@router.delete('/{learning_time_id}')
async def delete_learning_time(learning_time_id,
                               current_user=Depends(get_current_active_user),
                               db: Session = Depends(get_db)):
    user_id = current_user.uuid
    return crud.delete_learning_time(db=db,
                                     user_id=user_id,
                                     learning_time_id=learning_time_id,
                                     user_model=User,
                                     model=LearningTime)
