from fastapi import FastAPI

from app.routers import titles
app = FastAPI()

app.include_router(titles.router)
