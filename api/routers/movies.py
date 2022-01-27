from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import (
    database,
    schemas,
)
from ..repositories import movies as repo


router = APIRouter(
    prefix="/movies",
    tags=["movies"],
)


@router.get("/{movie_id}", response_model=schemas.MovieBase)
def get_a_movie(movie_id: int, db: Session = Depends(database.get_db)):
    db_movie = repo.get_movie(db, movie_id)

    return db_movie


@router.post("/")
def create_a_movie(
    movie: schemas.MovieBase,
    db: Session = Depends(database.get_db),
):
    return repo.create_movie(db, movie)


@router.put("/{movie_id}")
def update_a_movie(
    movie_id: int, updates: schemas.MovieBase, db: Session = Depends(database.get_db)
):
    return repo.update_movie(db, movie_id, updates)


@router.delete("/{movie_id}", status_code=200)
def delete_a_movie(movie_id: int, db: Session = Depends(database.get_db)):
    repo.delete_movie(db, movie_id)

    return {"status": "Data successfully deleted."}
