from fastapi import APIRouter
from .schedule import router as schedule_router

router = APIRouter()
router.include_router(schedule_router, prefix="/schedule")
