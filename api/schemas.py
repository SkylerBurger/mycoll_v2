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
