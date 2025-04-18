from fastapi import APIRouter, Path
from typing import Annotated
from schemas import Filter
from dotenv import load_dotenv
import requests
import os

router = APIRouter(prefix="/news/headlines", tags=["news"])

# load all environment variable
load_dotenv()
# NEWS API
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")


@router.get("/filter/")
def country_source_headlines(filter: Filter):
    """Fetch top headlines by filtering both country and source
    (use query parameters country and source)"""


@router.get("/country/{country_code}")
def country_code_headlines(country_code: Annotated[str, Path()]):
    """Fetch top headlines by country"""
    url = f"https://newsapi.org/v2/top-headlines?country={country_code}"
    response = requests.get(
        url,
        headers={"x-api-key": NEWSAPI_KEY},
    )
    return {"response": response.json()}


@router.get("/source/{source_id}")
def source_id_headlines(source_id):
    """Fetch top headlines by source"""
    url = f"https://newsapi.org/v2/top-headlines?sources={source_id}"
    response = requests.get(
        url,
        headers={"x-api-key": NEWSAPI_KEY},
    )
    return {"response": response.json()}
