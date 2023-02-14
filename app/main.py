from fastapi import FastAPI

from .routers import titles
app = FastAPI()

app.include_router(titles.router)
