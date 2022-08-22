from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

from models import OutputCurriculum, User
from cruds.curriculums import output_curriculums as crud


router = APIRouter()


@router.get('/{user_id}')
async def get_output_curriculums(user_id,
                                 db: Session = Depends(get_db)):
    return crud.get_output_curriculums(db=db,
                                       user_id=user_id,
                                       model=OutputCurriculum,
                                       user_model=User)
