from datetime import datetime, timedelta
from typing import Union

from fastapi import Depends, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import TokenData
from env import AUTH_SECRET_KEY


class Auth:
    _ALGORITHM = "HS256"
    _ACCESS_TOKEN_EXPIRE_MINUTES = 60

    _pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    _oauth2_scheme = OAuth2PasswordBearer(tokenUrl='v1/token')

    _credentials_exception = HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail='Cloud not validate credentials.',
        headers={'WWW=Authenticate': 'Bearer'}
    )

    @classmethod
    def verify_password(cls, plain_password, hashed_password):
        return cls._pwd_context.verify(plain_password, hashed_password)

    @classmethod
    def get_password_hash(cls, password):
        return cls._pwd_context.hash(password)

    @classmethod
    def get_user(cls, db: Session,
                 email: str,
                 model: User) -> User:
        try:
            user = db.query(model).filter(model.email == email).one_or_none()
        except Exception:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                                detail='Unrecognized email format.')
        if not user:
            raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                                detail='User not found.')
        return user

    @classmethod
    def authenticate_user(cls, db: Session,
                          email: str,
                          password: str,
                          model: User):
        user = cls.get_user(db=db, email=email, model=model)
        if not cls.verify_password(password, user.hashed_password):
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                                detail='Password is incorrect.')
        return user

    @classmethod
    def create_access_token(cls,
                            data: dict,
                            expires_delta: Union[timedelta, None] = None):
        to_encode = data.copy()

        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)

        to_encode.update({'exp': expire})
        encoded_jwt = jwt.encode(
            to_encode,
            AUTH_SECRET_KEY,
            algorithm=cls._ALGORITHM)
        return encoded_jwt

    @classmethod
    def get_current_user(cls,
                         db: Session = Depends(get_db),
                         token: str = Depends(_oauth2_scheme)):
        try:
            payload = jwt.decode(token,
                                 AUTH_SECRET_KEY,
                                 algorithms=[cls._ALGORITHM])
            email: str = payload.get('sub')
            if email is None:
                raise cls._credentials_exception
            token_data = TokenData(email=email)
        except JWTError:
            raise cls._credentials_exception

        user = cls._get_user(db=db, email=token_data.email, model=User)

        if user is None:
            raise cls._credentials_exception

        return user

    @classmethod
    def get_current_active_user(cls,
                                current_user: User = Depends(get_current_user)):
        return current_user

    @classmethod
    def login_for_access_token(cls,
                               db: Session,
                               model: User,
                               form_data: OAuth2PasswordRequestForm):
        user = cls._authenticate_user(db=db,
                                      email=form_data.username,
                                      password=form_data.password,
                                      model=model)
        if not user:
            raise HTTPException(status_code=HTTP_401_UNAUTHORIZED,
                                detail='Incorrect username or password.',
                                headers={'WWW-Authenticate': 'Bearer'})
        access_token_expires = timedelta(minutes=cls._ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = cls._create_access_token(
            data={'sub': user.email},
            expires_delta=access_token_expires
        )
        return {'access_token': access_token, 'token_type': 'bearer'}
