from fastapi import APIRouter

from app.api.routes import about
from app.api.routes import hello
from app.api.routes import projects

api_router = APIRouter()
api_router.include_router(hello.router)
api_router.include_router(about.router)
api_router.include_router(projects.router)
