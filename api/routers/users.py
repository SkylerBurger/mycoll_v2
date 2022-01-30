from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import (
    database,
    schemas,
)
from ..repositories import users as repo


router = APIRouter(
    prefix="/users",
)


@router.post("/", response_model=schemas.UserBase)
def create_user(
    user_signup: schemas.UserSignUp, db: Session = Depends(database.get_db)
):
    return repo.create_user(db, user_signup)
