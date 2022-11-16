from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from cruds.looking_backs import looking_backs as crud
from database import get_db

from models import LookingBack, User
import schemas

router = APIRouter()


@router.get('/{user_id}/this_week', response_model=schemas.LookingBack)
async def read_looking_backs_in_this_week(user_id,
                                          db: Session = Depends(get_db)):
    return crud.read_looking_back(
        db, model=LookingBack, user_model=User, user_id=user_id
    )


@router.get('/{user_id}', response_model=List[schemas.LookingBack])
async def read_looking_backs(user_id,
                             db: Session = Depends(get_db)):
    return crud.read_looking_backs(db=db,
                                   model=LookingBack,
                                   user_model=User,
                                   user_id=user_id)
