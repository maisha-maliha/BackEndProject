from fastapi import APIRouter


router = APIRouter(prefix="/news/headlines", tags=["news"])


@router.get("/filter/")
def source_id_headlines(filter):
    """Fetch top headlines by filtering both country and source
    (use query parameters country and source)"""


@router.get("/country/{country_code}")
def country_code_headlines(country_code):
    """Fetch top headlines by country"""


@router.get("/source/{source_id}")
def source_id_headlines(source_id):
    """Fetch top headlines by source"""
