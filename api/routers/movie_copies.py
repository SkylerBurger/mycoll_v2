from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import (
    auth,
    database,
    models,
    schemas,
)
from ..repositories import movie_copies as repo
from ..repositories.movies import checkout_movie_for_user

router = APIRouter(
    prefix="/moviecopies",
    tags=["movie_copies"],
    dependencies=[Depends(auth.oauth2_scheme)],
)


@router.post("/{movie_id}", response_model=schemas.MovieCopy)
def create_a_movie_copy(
    movie_id: int,
    movie_copy: schemas.MovieCopyBase,
    db: Session = Depends(database.get_db),
    user: models.User = Depends(auth.get_current_user),
):
    db_movie = checkout_movie_for_user(db, user, movie_id, "POST")
    return repo.create_movie_copy(db, db_movie, movie_copy, user)


@router.get("/{movie_copy_id}", response_model=schemas.MovieCopy)
def get_a_movie_copy(
    movie_copy_id: int,
    db: Session = Depends(auth.get_db),
    user: models.User = Depends(auth.get_current_user),
):
    return repo.checkout_movie_copy_for_user(db, user, movie_copy_id, "GET")


@router.put("/{movie_copy_id}", response_model=schemas.MovieCopy)
def update_a_movie_copy(
    movie_copy_id: int,
    movie_copy_update: schemas.MovieCopyUpdate,
    db: Session = Depends(auth.get_db),
    user: models.User = Depends(auth.get_current_user),
):
    return repo.update_movie_copy(db, movie_copy_id, movie_copy_update, user)
