import logging

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import (
    database,
    models,
    schemas,
)
from ..repositories import users as repo


router = APIRouter(
    prefix="/users",
)


@router.post("/signup", response_model=schemas.UserBase)
def sign_up(user_signup: schemas.UserSignUp, db: Session = Depends(database.get_db)):
    logging.info(user_signup)
    return repo.create_user(db, user_signup)
