from typing import Optional

from pydantic import BaseModel


class Movie(BaseModel):
    id: Optional[int]
    title: str
    release_year: int
    overview: Optional[str]
    mpaa_rating: Optional[str]
    runtime_minutes: int
    image_link: Optional[str]
    tmdb_page_link: Optional[str]


class MovieUpdate(BaseModel):
    title: Optional[str]
    release_year: Optional[int]
    overview: Optional[str]
    mpaa_rating: Optional[str]
    runtime_minutes: Optional[int]
    image_link: Optional[str]
    tmdb_page_link: Optional[str]