from sqlalchemy import Column, Integer, Text, String, Boolean

from .database import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    release_year = Column(Integer)
    overview = Column(Text)
    mpaa_rating = Column(String(255))
    runtime_minutes = Column(Integer)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True)
    hashed_password = Column(Text, nullable=True)
    email = Column(String(255), nullable=True)
    full_name = Column(String(255), nullable=True)
    disabled = Column(Boolean, nullable=True, default=False)
