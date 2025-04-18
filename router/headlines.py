from fastapi import APIRouter, Path, Query
from typing import Annotated
from schemas import Filter
from dotenv import load_dotenv
import requests
import os

router = APIRouter(prefix="/news/headlines", tags=["headlines"])

# load all environment variable
load_dotenv()
# NEWS API KEY from .env file
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")


@router.get("/filter")
def country_source_headlines(filter: Annotated[Filter, Query()]):
    """Fetch top headlines by filtering both country and source
    (use query parameters country and source)"""

    # newsapi url
    url = f"https://newsapi.org/v2/top-headlines?"

    if filter.country:
        url += f"country={filter.country}"

    # cannot have both country and source
    # if country then source is ignored
    if filter.source and not filter.country:
        url += f"sources={filter.source}"

    # fetch data from newsapi
    response = requests.get(
        url,
        headers={"x-api-key": NEWSAPI_KEY},
    )
    return {"response": response.json()}


@router.get("/country/{country_code}")
def country_code_headlines(country_code: Annotated[str, Path()]):
    """Fetch top headlines by country"""

    # newsapi url
    url = f"https://newsapi.org/v2/top-headlines?country={country_code}"

    # fetch data from newsapi
    response = requests.get(
        url,
        headers={"x-api-key": NEWSAPI_KEY},
    )
    return {"response": response.json()}


@router.get("/source/{source_id}")
def source_id_headlines(source_id):
    """Fetch top headlines by source"""

    # newsapi url
    url = f"https://newsapi.org/v2/top-headlines?sources={source_id}"

    # fetch data from newsapi
    response = requests.get(
        url,
        headers={"x-api-key": NEWSAPI_KEY},
    )
    return {"response": response.json()}
