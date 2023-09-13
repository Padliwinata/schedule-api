from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from db import db_asprak as db
from db.models import Asprak


router = APIRouter()


@router.get("/")
async def get_asprak():
    res = db.fetch()
    return {"message": "success", "code": 200, "data": res.items}

@router.post("/")
async def post_asprak(asprak: Asprak):
    db.put(jsonable_encoder(asprak))
    return {"message": "success", "code": 200, "data": jsonable_encoder(asprak)}

