from typing import Optional

from pydantic import BaseModel


class MovieBase(BaseModel):
    title: Optional[str] = None
    release_year: Optional[int] = None
    overview: Optional[str] = None
    mpaa_rating: Optional[str] = None
    runtime_minutes: Optional[int] = None

    class Config:
        orm_mode = True


class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True


class MovieCopyBase(BaseModel):
    platform: str
    form: str
    vod_link: Optional[str] = None

    class Config:
        orm_mode = True


class MovieCopyUpdate(BaseModel):
    platform: Optional[str] = None
    form: Optional[str] = None
    vod_link: Optional[str] = None


class MovieCopy(MovieCopyBase):
    id: int
    movie_id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None

    class Config:
        orm_mode = True


class UserSignUp(UserBase):
    password: str


class User(UserBase):
    id: int
    disabled: Optional[str] = None

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str
