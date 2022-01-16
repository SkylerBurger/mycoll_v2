from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from database import engine, SessionLocal

import crud
import models
import schemas


# I don't think I need this line since I manually created
# The tables using alembic
# models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# This is listed as a dependency. Is it called by someone?
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.get("/movies", response_model=List[schemas.Movie])
# def get_movie_list():
#     return movie_coll


@app.get("/movies/{movie_id}", response_model=schemas.Movie)
def get_a_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = crud.get_movie(db, movie_id)

    return db_movie


@app.post("/movies/")
def create_a_movie(movie: schemas.MovieBase, db: Session = Depends(get_db)):
    db_movie = crud.create_movie(db, movie)

    return db_movie


# @app.put("/movies/{movie_id}")
# def update_a_movie(movie_id: int, updates: schemas.MovieUpdate):
#     # Little funky below since we're in memory atm
#     movie = movie_coll[movie_id].dict()
#     updates = updates.dict()
#
#     for key, value in updates.items():
#         if value is not None:
#             movie[key] = value
#
#     movie_coll[movie_id] = schemas.Movie(**movie)
#
#     return movie_coll[movie_id]
#
#
# @app.delete("/movies/{movie_id}")
# def delete_a_movie(movie_id: int):
#     if movie_coll.get(movie_id):
#         del movie_coll[movie_id]
#         status = f"Deletion of Movie ID: {movie_id} successful."
#     else:
#         status = f"Movie ID: {movie_id} Not Found. Deletion was not performed."
#     return {"status": status}
