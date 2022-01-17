from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from database import SessionLocal

import crud
import schemas


app = FastAPI()


def get_db():
    """
    This function is like a fixture that is called as a dependency in routes
    that need a session connection to interact with the database.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/movies/{movie_id}", response_model=schemas.Movie)
def get_a_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = crud.get_movie(db, movie_id)

    return db_movie


@app.post("/movies/")
def create_a_movie(movie: schemas.MovieBase, db: Session = Depends(get_db)):
    db_movie = crud.create_movie(db, movie)

    return db_movie


@app.put("/movies/{movie_id}")
def update_a_movie(movie_id: int, updates: schemas.MovieBase, db: Session = Depends(get_db)):
    db_movie = crud.update_movie(db, movie_id, updates)

    return db_movie


@app.delete("/movies/{movie_id}", status_code=200)
def delete_a_movie(movie_id: int, db: Session = Depends(get_db)):
    crud.delete_movie(db, movie_id)

    return {"status": "Data successfully deleted."}
