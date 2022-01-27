from sqlalchemy.orm import Session

from .. import (
    models,
    schemas,
)


def get_movie(db: Session, movie_id: int) -> models.Movie:
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()


def create_movie(db: Session, movie: schemas.MovieBase) -> models.Movie:
    db_movie = models.Movie(
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


def update_movie(
    db: Session, movie_id: int, updates: schemas.MovieBase
) -> models.Movie:
    db_movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()

    # There is probably a better way to update than this
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


def delete_movie(db: Session, movie_id: int):
    db_movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    db.delete(db_movie)
    db.commit()
