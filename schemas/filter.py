from pydantic import BaseModel


# for filtering top headlines by country and source
class Filter(BaseModel):
    country: str | None = None
    source: str | None = None
