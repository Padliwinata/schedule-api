from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
from yattag import Doc
from db.models import Jadwal
from db import db_jadwal as db

router = APIRouter()

@router.get("/courses", response_class=HTMLResponse)
async def get_courses():
    doc, tag, text = Doc().tagtext()
    # with tag('div', klass='courses-container col-md-4'):
    with tag('div', klass='course'):
        with tag('div', klass='course-preview'):
            with tag('h6'):
                text('PEMROGRAMAN WEB')
            with tag('h4'):
                text('WEBPRO')
        with tag('div', klass='course-info'):
            with tag('h5'):
                text('Link Penting')
            with tag('a', href='#'):
                with tag('h6'):
                    text('CONTOH2')
    return doc.getvalue()

@router.get("/example", response_class=HTMLResponse)
async def get_example():
    doc, tag, text = Doc().tagtext()
    with tag('div', klass='courses-container col-md-4'):
        text('example')
    return doc.getvalue()
        
