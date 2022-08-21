from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from cruds.looking_backs import looking_backs as crud
from database import get_db

from models import LookingBack, User
import schemas

router = APIRouter()


@router.get('/{user_id}/this_week')
async def read_looking_backs_in_this_week(user_id,
                                          db: Session = Depends(get_db)):
    return crud.read_looking_back(
        db, model=LookingBack, user_model=User, user_id=user_id
    )


@router.get('/{user_id}')
async def read_looking_backs(user_id,
                             db: Session = Depends(get_db)):
    return crud.read_looking_backs(db=db,
                                   model=LookingBack,
                                   user_model=User,
                                   user_id=user_id)


@router.post('/{user_id}')
async def create_looking_back(params: schemas.LookingBackCreate,
                              user_id,
                              db: Session = Depends(get_db)):
    return crud.create_looking_back(params=params,
                                    user_id=user_id,
                                    model=LookingBack,
                                    db=db)


@router.put('/{user_id}/{looking_back_id}')
async def update_looking_back(user_id: str,
                              looking_back_id: str,
                              params: schemas.LookingBack,
                              db: Session = Depends(get_db)):
    return crud.update_looking_back(db=db,
                                    user_id=user_id,
                                    looking_back_id=looking_back_id,
                                    params=params,
                                    user_model=User,
                                    model=User)
