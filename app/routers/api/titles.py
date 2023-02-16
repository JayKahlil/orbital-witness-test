from fastapi import APIRouter

from app.routers.models.full_title import FullTitle
from app.routers.models.titles_list import TitlesList
from app.handlers.title_handler import list_titles, get_title_by_id

router = APIRouter(
    prefix="/api/titles",
    tags=["titles"],
)


@router.get("/", responses={400: {"description": "Invalid request configuration"}})
def get_titles(
        _page: int = 1, _limit: int = 10, _sort: str = "id", _order: str = "asc",
        title_class: str | None = None) -> TitlesList:
    titles, total_titles = list_titles(_page, _limit, _sort, _order, title_class)

    response = TitlesList(titles=titles, page=_page, page_size=_limit, total_titles=total_titles)

    return response


@router.get("/{id}", responses={404: {"description": "Title not found"}})
def get(id: str) -> FullTitle:
    return get_title_by_id(id)
