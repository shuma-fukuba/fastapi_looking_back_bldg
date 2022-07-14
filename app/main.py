from fastapi import FastAPI, APIRouter
from typing import List
import env

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
    prefix='v1',
)
