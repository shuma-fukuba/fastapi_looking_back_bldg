from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from modules.auth.auth import get_current_active_user
from models import OutputCurriculum, User, UsersOutputCurriculums
from cruds.curriculums import output_curriculums as crud
import schemas


router = APIRouter()


@router.get('/')
async def get_output_curriculums(current_user: User = Depends(get_current_active_user),
                                 db: Session = Depends(get_db)):
    return crud.get_output_curriculums(db=db,
                                       user_id=current_user.uuid,
                                       model=OutputCurriculum,
                                       user_model=User)


@router.get('/{curriculum_id}')
async def get_input_curriculum(curriculum_id,
                               current_user: User = Depends(
                                   get_current_active_user),
                               db: Session = Depends(get_db)):
    return crud.get_output_curriculum(db=db,
                                      user_id=current_user.uuid,
                                      curriculum_id=curriculum_id,
                                      model=OutputCurriculum,
                                      association_model=UsersOutputCurriculums,
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
                                       model=UsersOutputCurriculums)
