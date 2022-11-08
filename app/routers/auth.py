from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import User
from modules.auth import auth

import schemas


router = APIRouter()


@router.post('/', response_model=schemas.Token)
async def login_for_access_token(params: schemas.CreateTokenSchema,
                                 db: Session = Depends(get_db)):
    return auth.login_for_access_token(db=db,
                                       model=User,
                                       form_data=params)
