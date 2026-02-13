from fastapi import APIRouter


router = APIRouter()


@router.get("/about")
async def about():
    return {"pseudo": "t11prh96"}
