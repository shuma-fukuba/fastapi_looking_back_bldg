from fastapi import APIRouter, Depends
from models import User
from modules.auth.auth import get_current_active_user
import schemas
from .looking_backs import router as looking_backs_router
from .learning_time import router as learning_time_router
from .input_curriculum import router as input_curriculum_router
from .output_curriculum import router as output_curriculum_router
from .home import router as home_router

router = APIRouter()


@router.get('/', response_model=schemas.User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


router.include_router(
    looking_backs_router,
    prefix='/looking_backs',
)

router.include_router(
    learning_time_router,
    prefix='/learning_times'
)

router.include_router(
    input_curriculum_router,
    prefix='/input_curriculums'
)

router.include_router(
    output_curriculum_router,
    prefix='/output_curriculums'
)

router.include_router(
    home_router,
    prefix='/home'
)
