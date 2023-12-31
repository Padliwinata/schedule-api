from fastapi import APIRouter
from .jadwal import router as jadwal_router
from .asprak import router as asprak_router
from .htmx import router as htmx_router

router = APIRouter()
router.include_router(jadwal_router, prefix="/jadwal")
router.include_router(asprak_router, prefix="/asprak")
router.include_router(htmx_router, prefix="/hx")
