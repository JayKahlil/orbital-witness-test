from pydantic import BaseModel


class BaseTitle(BaseModel):
    id: str
    title_number: str
    title_class: str
