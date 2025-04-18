from fastapi import FastAPI
from router import news_router, headlines_router, auth_router


# create fastAPI application
app = FastAPI()

# add routes
app.include_router(auth_router)
app.include_router(news_router)
app.include_router(headlines_router)
