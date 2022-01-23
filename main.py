from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from database import SessionLocal

import crud
import schemas


app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


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


def fake_decode_user(token: str):
    return schemas.User(username=token + "fake_decoded", email="test@test.com")


def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_user(token)
    return user


@app.get("/users/me")
def read_users_me(current_user: schemas.User = Depends(get_current_user)):
    return current_user


@app.get("/movies/{movie_id}", response_model=schemas.Movie)
def get_a_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = crud.get_movie(db, movie_id)

    return db_movie


@app.post("/movies/")
def create_a_movie(movie: schemas.MovieBase, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    print(token)
    db_movie = crud.create_movie(db, movie)

    return db_movie


@app.put("/movies/{movie_id}")
def update_a_movie(
    movie_id: int, updates: schemas.MovieBase, db: Session = Depends(get_db)
):
    db_movie = crud.update_movie(db, movie_id, updates)

    return db_movie


@app.delete("/movies/{movie_id}", status_code=200)
def delete_a_movie(movie_id: int, db: Session = Depends(get_db)):
    crud.delete_movie(db, movie_id)

    return {"status": "Data successfully deleted."}
