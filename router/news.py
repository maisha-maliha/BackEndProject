from fastapi import APIRouter, Query
from typing import Annotated
from dotenv import load_dotenv
import requests
import os

# load all environment variables
load_dotenv()

NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

router = APIRouter(prefix="/news", tags=["news"])


@router.get("")
def news(
    q: Annotated[str, Query()],
    pageSize: Annotated[int | None, Query()] = None,
    page: Annotated[int | None, Query()] = None,
):
    """Fetch all news with pagination support"""
    url = f"https://newsapi.org/v2/everything?q={q}"
    if pageSize:
        url += f"&pageSize={pageSize}"
    if pageSize:
        url += f"&page={page}"
    print(NEWSAPI_KEY)
    response = requests.get(
        url,
        headers={"x-api-key": NEWSAPI_KEY},
    )
    return {"response": response.json()}


@router.post("/save-latest")
def save_lates():
    """Fetch the latest news and save the top 3 into a database."""
