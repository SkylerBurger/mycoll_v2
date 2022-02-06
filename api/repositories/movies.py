from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import (
    models,
    schemas,
)


def get_movies_by_user(db: Session, user: models.User) -> List[schemas.Movie]:
    return db.query(models.Movie).filter(models.Movie.owner_id == user.id).all()


def create_movie(
    db: Session, movie: schemas.MovieBase, user: models.User
) -> models.Movie:
    db_movie = models.Movie(
        owner_id=user.id,
        title=movie.title,
        release_year=movie.release_year,
        overview=movie.overview,
        mpaa_rating=movie.mpaa_rating,
        runtime_minutes=movie.runtime_minutes,
    )

    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)

    return db_movie


def checkout_movie_for_user(
    db: Session, user: models.User, movie_id: int, operation: str
):
    """
    This function fetches a movie from the database and only returns it if the
    current user.id matches the owner_id of that movie.
    """
    db_movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if not db_movie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not Found: Movie with ID of {movie_id}",
        )
    if not db_movie.owner_id == user.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Unauthorized {operation}: Movie does not belong to current user.",
        )

    return db_movie


def update_movie(
    db: Session, user: models.User, movie_id: int, updates: schemas.MovieBase
) -> models.Movie:
    db_movie = checkout_movie_for_user(db, user, movie_id, "PUT")

    if updates.title is not None:
        db_movie.title = updates.title
    if updates.overview is not None:
        db_movie.overview = updates.overview
    if updates.mpaa_rating is not None:
        db_movie.mpaa_rating = updates.mpaa_rating
    if updates.runtime_minutes is not None:
        db_movie.runtime_minutes = updates.runtime_minutes

    db.commit()
    db.refresh(db_movie)

    return db_movie


def delete_movie(db: Session, user: models.User, movie_id: int):
    db_movie = checkout_movie_for_user(db, user, movie_id, "DELETE")
    db.delete(db_movie)
    db.commit()

    return {"status": "Data successfully deleted."}
