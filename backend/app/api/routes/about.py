import json
from pathlib import Path

from fastapi import APIRouter

from app.schemas.about import About

router = APIRouter()

DB_PATH = Path(__file__).parents[4] / "data" / "db.json"


@router.get("/about", response_model=About)
async def about():
    with open(DB_PATH) as f:
        data = json.load(f)
    return data["about"]
