from fastapi import APIRouter

from .models.titles_list import TitlesList
from ..handlers.title_handler import list_titles

router = APIRouter(
    prefix="/api/titles",
    tags=["titles"],
)


@router.get("/")
def get_titles(
        _page: int = 1, _limit: int = 10, _sort: str = "id", _order: str = "asc",
        title_class: str | None = None) -> TitlesList:
    titles, total_titles = list_titles(_page, _limit, _sort, _order, title_class)

    response = TitlesList(titles=titles, page=_page, page_size=_limit, total_titles=total_titles)

    return response
