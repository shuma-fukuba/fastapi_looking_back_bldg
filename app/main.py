import env
from starlette.middleware.base import BaseHTTPMiddleware
from middlewares import http_log
from fastapi import FastAPI, APIRouter
from routers.looking_backs import router as looking_backs_router
from routers.learning_time import router as learning_time_router
from routers.home import router as home_router
from routers.curriculums import router as curriculum_router
from routers.user import router as user_router
from routers.auth import router as auth_router


router = APIRouter()

router.include_router(
    looking_backs_router,
    prefix='/looking_backs',
    tags=['looking_backs']
)

router.include_router(
    learning_time_router,
    prefix='/learning_time',
    tags=['learning_time']
)

router.include_router(
    home_router,
    prefix='/home',
    tags=['home']
)

router.include_router(
    curriculum_router,
    prefix='/curriculums',
    tags=['curriculums']
)

router.include_router(
    user_router,
    prefix='/users',
    tags=['users']
)

router.include_router(
    auth_router,
    prefix='/token',
    tags=['token']
)

if env.APP_ENV == 'development':
    app = FastAPI()
else:
    app = FastAPI(
        docs_url=None,
        redoc_url=None,
        openapi_url=None
    )

app.include_router(
    router,
    prefix='/v1',
)

app.add_middleware(BaseHTTPMiddleware, dispatch=http_log)
