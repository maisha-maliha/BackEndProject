from pydantic import BaseModel, HttpUrl
from datetime import date


class Article(BaseModel):
    title: str
    description: str
    url: HttpUrl
    published_at: date
