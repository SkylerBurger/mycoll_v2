from sqlalchemy import Column, Integer, Text, String
from database import MyCollDeclarativeBase


class Movie(MyCollDeclarativeBase):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    release_year = Column(Integer)
    overview = Column(Text)
    mpaa_rating = Column(String(255))
    runtime_minutes = Column(Integer)


class MyCollUser(MyCollDeclarativeBase):
    __tablename__ = 'mycoll_users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    age = Column(Integer)