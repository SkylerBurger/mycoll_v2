from typing import List

from fastapi import FastAPI

from database import engine, session
import models
import schemas


models.MyCollDeclarativeBase.metadata.create_all(bind=engine)
app = FastAPI()


# Collection in memory for initial testing
# TODO: Get real DB action going with SQLAlchemy
movie_coll = {
    1: schemas.Movie(
        id=1,
        title="Sphere",
        release_year=1988,
        overview="Something's up in the water.",
        mpaa_rating="R",
        runtime_minutes=120
    )
}


@app.get("/movies", response_model=List[schemas.Movie])
def get_movie_list():
    return movie_coll


@app.get("/movies/{movie_id}", response_model=schemas.Movie)
def get_a_movie(movie_id: int):
    movie = movie_coll.get(movie_id)

    if movie is not None:
        response = movie_coll[movie_id]
    else:
        response = {"Status": f"Movie ID: {movie_id} Not Found"}

    return response


@app.post("/movies/{movie_id}")
def create_a_movie(movie_id: int, movie: schemas.Movie):
    movie.id = movie_id
    movie_coll[movie_id] = movie
    return movie_coll[movie_id]


@app.put("/movies/{movie_id}")
def update_a_movie(movie_id: int, updates: schemas.MovieUpdate):
    # Little funky below since we're in memory atm
    movie = movie_coll[movie_id].dict()
    updates = updates.dict()

    for key, value in updates.items():
        if value is not None:
            movie[key] = value

    movie_coll[movie_id] = schemas.Movie(**movie)

    return movie_coll[movie_id]


@app.delete("/movies/{movie_id}")
def delete_a_movie(movie_id: int):
    if movie_coll.get(movie_id):
        del movie_coll[movie_id]
        status = f"Deletion of Movie ID: {movie_id} successful."
    else:
        status = f"Movie ID: {movie_id} Not Found. Deletion was not performed."
    return {"status": status}
