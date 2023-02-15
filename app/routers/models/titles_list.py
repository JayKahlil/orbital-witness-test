from pydantic import BaseModel

from app.routers.models.base_title import BaseTitle


class TitlesList(BaseModel):
    titles: list[BaseTitle]
    page: int
    page_size: int
    total_titles: int
