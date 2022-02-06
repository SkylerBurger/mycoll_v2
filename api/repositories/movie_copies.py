from sqlalchemy.orm import Session

from .. import (
    models,
    schemas,
)


def create_movie_copy(
        db: Session,
        db_movie: models.Movie,
        movie_copy: schemas.MovieCopyBase,
        user: models.User
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
