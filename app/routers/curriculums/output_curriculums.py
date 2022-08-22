from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

from models import OutputCurriculum, User, UsersOutputCurriculums
from cruds.curriculums import output_curriculums as crud
import schemas


router = APIRouter()


@router.get('/{user_id}')
async def get_output_curriculums(user_id,
                                 db: Session = Depends(get_db)):
    return crud.get_output_curriculums(db=db,
                                       user_id=user_id,
                                       model=OutputCurriculum,
                                       user_model=User)


@router.get('/{user_id}/{curriculum_id}')
async def get_input_curriculum(user_id,
                               curriculum_id,
                               db: Session = Depends(get_db)):
    return crud.get_output_curriculum(db=db,
                                      user_id=user_id,
                                      curriculum_id=curriculum_id,
                                      model=OutputCurriculum,
                                      association_model=UsersOutputCurriculums,
                                      user_model=User)


@router.put('/{user_id}/{curriculum_id}')
async def udpate_curriculum_done(user_id,
                                 curriculum_id,
                                 params: schemas.UpdateCurriculumSchema,
                                 db: Session = Depends(get_db)):
    done = params.done
    return crud.udpate_curriculum_done(db=db,
                                       user_id=user_id,
                                       curriculum_id=curriculum_id,
                                       done=done,
                                       model=UsersOutputCurriculums)
