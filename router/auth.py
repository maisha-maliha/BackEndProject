from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from utils import hash_password, verify_password, create_token, decode_token
from typing import Annotated
import datetime

# password = testuser
user = {"maisha": "$2b$12$7XqBMcxvK3H9LL13f5ue8epKoXqFPUzanZAcsPQ5TusM5U7Ye0Icq"}

# router
router = APIRouter(prefix="", tags=["Auth"])
oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/token")
def token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):

    if form_data.username in user:
        if verify_password(form_data.password, user[form_data.username]):
            expiry_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
            token_creation = create_token({"username": form_data.username})
            return {
                "access_token": token_creation,
                "token_type": "bearer",
                "exp": expiry_time,
            }
    # if auth not match with user then raise error
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )
