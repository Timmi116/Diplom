from fastapi import FastAPI
from app.database import init_database
from app.views import router

app = FastAPI()
init_database()
app.include_router(router)