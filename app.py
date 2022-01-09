from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Movie(BaseModel):
    title: str
    release_year: int
    overview: Optional[str]
    mpaa_rating: Optional[str]
    runtime_minutes: int
    image_link: Optional[str]
    tmdb_page_link: Optional[str]


movie_coll = {
    1: Movie(
        title="Sphere",
        release_year=1988,
        overview="Something's up in the water.",
        mpaa_rating="R",
        runtime_minutes=120
    )
}


@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    return movie_coll[movie_id]
