from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from db.models import Jadwal
from db import db


router = APIRouter(prefix="/schedule")


@router.get("/")
async def get_schedule():
    res = db.fetch()
    return {"message": "success", "code": 200, "data": res.items}


@router.post("/")
async def post_schedule(jadwal: Jadwal):
    db.put(jsonable_encoder(jadwal))
    return {"message": "success", "code": 200, "data": jadwal}
