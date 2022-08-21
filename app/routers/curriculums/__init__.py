from fastapi import APIRouter
from .input_curriculums import router as input_router
from .output_curriculums import router as output_router


router = APIRouter()


router.include_router(
    input_router,
    prefix='/input'
)

router.include_router(
    output_router,
    prefix='/outputs'
)
