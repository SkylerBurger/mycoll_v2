from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from .repositories import users as repo
from .schemas import UserBase


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


def get_hashed_password(plain_password: str) -> str:
    return pwd_context.hash(plain_password)


def authenticate_user(username: str, password: str):
    db_user = repo.get_user(username)

    if not db_user:
        return False

    if not verify_password(password, db_user.hashed_password):
        return False

    return db_user


def fake_user_from_token(token):
    fake_name = f"{token}_fake"
    return UserBase(
        username=fake_name,
        email="test@test.com",
        full_name="Norville Rogers",
    )


def get_current_user(token: str = Depends(oauth2_scheme)):
    return fake_user_from_token(token)
