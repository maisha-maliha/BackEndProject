from fastapi import APIRouter

router = APIRouter(prefix="/news", tags=["news"])


@router.get("")
def news():
    """Fetch all news with pagination support"""


@router.post("/save-latest")
def save_lates():
    """Fetch the latest news and save the top 3 into a database."""
