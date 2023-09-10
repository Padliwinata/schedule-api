from fastapi import APIRouter
from deta import Deta


router = APIRouter(prefix="/schedule")


@router.get("/")
async def get_schedule():
    return {"message": "hello"}
