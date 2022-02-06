from sqlalchemy.orm import relationship
from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Text,
)

from .database import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String(255))
    release_year = Column(Integer)
    overview = Column(Text)
    mpaa_rating = Column(String(255))
    runtime_minutes = Column(Integer)


class MovieCopy(Base):
    __tablename__ = "movie_copies"

    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    owner_id = Column(Integer, ForeignKey("users.id"))
    platform = Column(String(255))
    form = Column(String(255))
    vod_link = Column(String(255), nullable=True)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True)
    hashed_password = Column(Text, nullable=True)
    email = Column(String(255), nullable=True)
    full_name = Column(String(255), nullable=True)
    disabled = Column(Boolean, nullable=True, default=False)
    movies = relationship("Movie")
