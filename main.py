from fastapi import FastAPI

from app.routers.gui import titles_gui
from app.routers.api import titles

app = FastAPI()

app.include_router(titles.router)
app.include_router(titles_gui.router)
