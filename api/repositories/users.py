from sqlalchemy.orm import Session

from .. import (
    auth,
    models,
    schemas,
)


def create_user(db: Session, user_signup: schemas.UserSignUp) -> models.User:
    hashed_password = auth.get_hashed_password(user_signup.password)

    db_user = models.User(
        username=user_signup.username,
        hashed_password=hashed_password,
        full_name=user_signup.full_name,
        email=user_signup.email,
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user_by_username(db: Session, username: str) -> models.User:
    return db.query(models.User).filter(models.User.username == username).one()
