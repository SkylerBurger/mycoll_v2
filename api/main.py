from dotenv import load_dotenv
from fastapi import FastAPI

from . import auth
from .routers import (
    movies,
    users,
)


load_dotenv()

app = FastAPI()
app.include_router(auth.router)
app.include_router(movies.router)
app.include_router(users.router)
