from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from models import User
from modules.auth import Auth
import schemas


router = APIRouter()


@router.post('/', response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                                 db: Session = Depends(get_db)):
    return Auth.login_for_access_token(db=db,
                                       model=User,
                                       form_data=form_data)
