from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import schemas
from models import User, LookingBack
from cruds.looking_backs import looking_backs as crud
from database import get_db
from modules.auth.auth import get_current_active_user

router = APIRouter()


@router.get('/', response_model=List[schemas.LookingBack])
async def read_looking_backs(current_user: User = Depends(get_current_active_user),
                             db: Session = Depends(get_db)):
    return crud.read_looking_backs(db=db,
                                   model=LookingBack,
                                   user_model=User,
                                   user_id=current_user.uuid)


@router.post('/', response_model=schemas.LookingBack)
async def create_looking_back(params: schemas.LookingBackCreate,
                              current_user=Depends(get_current_active_user),
                              db: Session = Depends(get_db)):
    user_id = current_user.uuid
    return crud.create_looking_back(params=params,
                                    user_id=user_id,
                                    model=LookingBack,
                                    db=db)


@router.get('/this_week', response_model=schemas.LookingBack)
async def read_looking_backs_in_this_week(current_user: User = Depends(get_current_active_user),
                                          db: Session = Depends(get_db)):
    return crud.read_looking_back(
        db, model=LookingBack, user_model=User, user_id=current_user.uuid
    )


@router.put('/{looking_back_id}')
async def update_looking_back(looking_back_id: str,
                              params: schemas.LookingBack,
                              current_user: User = Depends(
                                  get_current_active_user),
                              db: Session = Depends(get_db)):
    user_id = current_user.uuid
    return crud.update_looking_back(db=db,
                                    user_id=user_id,
                                    looking_back_id=looking_back_id,
                                    params=params,
                                    user_model=User,
                                    model=User)


@router.delete('/{looking_back_id}')
async def delete_looking_back(looking_back_id: str,
                              current_user: User = Depends(
                                  get_current_active_user),
                              db: Session = Depends(get_db)):
    user_id = current_user.uuid
    return crud.delete_looking_back(db=db,
                                    user_id=user_id,
                                    looking_back_id=looking_back_id,
                                    model=LookingBack,
                                    user_model=User)
