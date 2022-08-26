from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from modules.auth.auth import get_current_active_user
from models import InputCurriculum, User, UsersInputCurriculums
from cruds.curriculums import input_curriculums as crud
import schemas


router = APIRouter()


@router.get('/{user_id}')
async def get_input_curriculums(user_id,
                                current_user=Depends(get_current_active_user),
                                db: Session = Depends(get_db)):
    return crud.get_input_curriculums(db=db,
                                      user_id=user_id,
                                      model=InputCurriculum,
                                      user_model=User)


@router.get('/{user_id}/{curriculum_id}')
async def get_input_curriculum(user_id,
                               curriculum_id,
                               current_user=Depends(get_current_active_user),
                               db: Session = Depends(get_db)):
    return crud.get_input_curriculum(db=db,
                                     user_id=user_id,
                                     curriculum_id=curriculum_id,
                                     model=InputCurriculum,
                                     association_model=UsersInputCurriculums,
                                     user_model=User)


@router.put('/{curriculum_id}')
async def udpate_curriculum_done(curriculum_id,
                                 params: schemas.UpdateCurriculumSchema,
                                 current_user=Depends(get_current_active_user),
                                 db: Session = Depends(get_db)):
    done = params.done
    user_id = current_user.uuid
    return crud.udpate_curriculum_done(db=db,
                                       user_id=user_id,
                                       curriculum_id=curriculum_id,
                                       done=done,
                                       model=UsersInputCurriculums)
