from pydantic import BaseModel, HttpUrl


class Article(BaseModel):
    title: str
    description: str
    url: HttpUrl
    published_at: str
