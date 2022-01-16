from typing import Optional

from pydantic import BaseModel


class MovieBase(BaseModel):
    title: Optional[str]
    release_year: Optional[int]
    overview: Optional[str]
    mpaa_rating: Optional[str]
    runtime_minutes: Optional[int]


class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True


class MyCollUserBase(BaseModel):
    name: str
    age: int


class MyCollUser(MyCollUserBase):
    id: int

    class Config:
        orm_mode = True
