from fastapi import APIRouter, Query, Depends
from typing import Annotated
from dotenv import load_dotenv
from models import add_news
from schemas import Article
from .auth import oauth_scheme
import requests
import os

# load all environment variables
load_dotenv()

NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

router = APIRouter(prefix="/news", tags=["news"])


@router.get("")
def news(
    q: Annotated[str, Query()],
    token: Annotated[str, Depends(oauth_scheme)],
    pageSize: Annotated[int | None, Query()] = None,
    page: Annotated[int | None, Query()] = None,
):
    """Fetch all news with pagination support"""

    # newsapi url
    url = f"https://newsapi.org/v2/everything?q={q}"
    if pageSize:
        url += f"&pageSize={pageSize}"
    if pageSize:
        url += f"&page={page}"

    # fetch data from newsapi
    response = requests.get(
        url,
        headers={"x-api-key": NEWSAPI_KEY},
    )
    return {"response": response.json()}


@router.post("/save-latest")
def save_latest(
    token: Annotated[str, Depends(oauth_scheme)],
):
    """Fetch the latest news and save the top 3 into a database."""

    # newsapi url
    url = f"https://newsapi.org/v2/top-headlines?country=us&pageSize=3"

    # fetch data from newsapi
    response = requests.get(
        url,
        headers={"x-api-key": NEWSAPI_KEY},
    ).json()

    artilces = []
    for item in response["articles"]:

        article = Article(
            title=item["title"],
            description=item["description"],
            url=item["url"],
            published_at=item["publishedAt"],
        )
        artilces.append(article)

    # add data to table
    added = add_news(artilces)

    return {
        "response": (
            "sucessfully added data" if added else "couldnt add data to database"
        ),
        "data": artilces,
    }
