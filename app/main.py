from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router


app = FastAPI(
    title="API Praktikum IFLab",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
