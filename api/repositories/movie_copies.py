from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import (
    models,
    schemas,
)


def checkout_movie_copy_for_user(
    db: Session, user: models.User, movie_copy_id: int, operation: str
):
    db_movie_copy = (
        db.query(models.MovieCopy).filter(models.MovieCopy.id == movie_copy_id).one()
    )
    if not db_movie_copy:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not Found: Movie Copy with ID of {movie_copy_id}",
        )
    if not db_movie_copy.owner_id == user.id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Unauthorized {operation}: Movie Copy does not belong to current user.",
        )

    return db_movie_copy


def create_movie_copy(
    db: Session,
    db_movie: models.Movie,
    movie_copy: schemas.MovieCopyBase,
    user: models.User,
):
    db_movie_copy = models.MovieCopy(
        movie_id=db_movie.id,
        owner_id=user.id,
        platform=movie_copy.platform,
        form=movie_copy.form,
        vod_link=movie_copy.vod_link,
    )
    db.add(db_movie_copy)
    db.commit()
    db.refresh(db_movie_copy)

    return db_movie_copy


def update_movie_copy(
    db: Session,
    movie_copy_id: int,
    updates: schemas.MovieCopyUpdate,
    user: models.User,
):
    db_movie_copy = checkout_movie_copy_for_user(db, user, movie_copy_id, "PUT")

    if updates.platform is not None:
        db_movie_copy.platform = updates.platform
    if updates.form is not None:
        db_movie_copy.form = updates.form
    if updates.vod_link is not None:
        db_movie_copy.vod_link = updates.vod_link

    db.commit()
    db.refresh(db_movie_copy)

    return db_movie_copy
