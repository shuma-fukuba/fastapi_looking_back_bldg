from datetime import datetime, timedelta
from typing import Union

from fastapi import Depends, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from models import User
from schemas import TokenData


SECRET_KEY = "13774feb78b891056fafbb00676f2ee6aa480797fb3bb7dbeb77e5004fdb04aa"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


def veirfy_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db: Session,
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


def authenticate_user(db: Session,
                      email: str,
                      password: str,
                      model: User):
    user = get_user(db=db, email=email, model=model)
    if not veirfy_password(password, user.hashed_password):
        return False
    return user


def create_access_token(
        data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime().utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(db: Session, token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail='Cloud not validate credentials.',
        headers={'WWW=Authenticate': 'Bearer'}
    )

    try:
        paylod = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = paylod.get('sub')
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception

    user = get_user(db=db, email=token_data.email)

    if user is None:
        raise credentials_exception

    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                            detail='Inactive user.')
    return current_user


async def login_for_access_token(db: Session,
                                 model: User,
                                 form_data: OAuth2PasswordRequestForm):
    user = authenticate_user(db=db,
                             email=form_data.email,
                             password=form_data.password,
                             model=model)
    if not user:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED,
                            detail='Incorrect username or password.',
                            headers={'WWW-Authenticate': 'Bearer'})
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={'sub': user.email},
        expires_delta=access_token_expires
    )
    return {'access_token': access_token, 'token_type': 'bearer'}
