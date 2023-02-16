from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from ...handlers.title_handler import list_titles, get_title_by_id

router = APIRouter(
    prefix="/gui/titles",
    tags=["titles"],
)

templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
def get_titles(request: Request, _page: int = 1, _limit: int = 10, _sort: str = "id", _order: str = "asc",
               title_class: str | None = None):
    titles, total_titles = list_titles(_page, _limit, _sort, _order, title_class)

    return templates.TemplateResponse("titles.html", {
        "request": request,
        "titles": titles,
        "page": _page,
        "limit": _limit,
        "total_titles": total_titles
    })


@router.get("/{id}", response_class=HTMLResponse)
def get(request: Request, id: str):
    return templates.TemplateResponse("title.html", {"request": request, "title": get_title_by_id(id)})
