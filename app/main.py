import env
from starlette.middleware.base import BaseHTTPMiddleware
from middlewares import http_log
from fastapi import FastAPI, APIRouter

router = APIRouter()

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
