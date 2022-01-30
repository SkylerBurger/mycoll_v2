from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import (
    auth,
    database,
    models,
    schemas,
)
from ..repositories import movies as repo


router = APIRouter(
    prefix="/movies", tags=["movies"], dependencies=[Depends(auth.oauth2_scheme)]
)


@router.get("/", response_model=List[schemas.Movie])
def get_movies_by_user(
    user: models.User = Depends(auth.get_current_user),
    db: Session = Depends(database.get_db),
):
    return repo.get_movies_by_user(db, user)


@router.get("/{movie_id}", response_model=schemas.MovieBase)
def get_a_movie(
    movie_id: int,
    db: Session = Depends(database.get_db),
    user: models.User = Depends(auth.get_current_user)
):
    return repo.checkout_movie_for_user(db, user, movie_id, "GET")


@router.post("/", response_model=schemas.Movie)
def create_a_movie(
    movie: schemas.MovieBase,
    db: Session = Depends(database.get_db),
    user: models.User = Depends(auth.get_current_user),
):
    return repo.create_movie(db, movie, user)


@router.put("/{movie_id}", response_model=schemas.MovieBase)
def update_a_movie(
    movie_id: int,
    updates: schemas.MovieBase,
    db: Session = Depends(database.get_db),
    user: models.User = Depends(auth.get_current_user),
):
    return repo.update_movie(db, user, movie_id, updates)


@router.delete("/{movie_id}", status_code=200)
def delete_a_movie(
    movie_id: int,
    db: Session = Depends(database.get_db),
    user: models.User = Depends(auth.get_current_user),
):
    return repo.delete_movie(db, user, movie_id)
