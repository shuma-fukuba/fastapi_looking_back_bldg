from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from models import User
from modules.auth import auth

import schemas


router = APIRouter()


@router.post('/', response_model=schemas.Token)
async def login_for_access_token(db: Session = Depends(get_db),
                                 form_data: OAuth2PasswordRequestForm = Depends()):
    return auth.login_for_access_token(db=db,
                                       model=User,
                                       form_data=form_data)
