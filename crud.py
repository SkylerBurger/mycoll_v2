from sqlalchemy.orm import Session

import models
import schemas


def get_movie(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()

def create_movie(db: Session, movie: schemas.MovieBase):
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
