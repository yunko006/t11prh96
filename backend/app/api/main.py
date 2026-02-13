from fastapi import APIRouter

from app.api.routes import hello
from app.api.routes import about

api_router = APIRouter()
api_router.include_router(hello.router)
api_router.include_router(about.router)
