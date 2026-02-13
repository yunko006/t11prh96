from fastapi import FastAPI

from app.api.main import api_router

app = FastAPI(title="T11PRH96 Backend", version="0.1.0")

app.include_router(api_router)
