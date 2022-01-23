from sqlalchemy import Column, Integer, Text, String

from database import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    release_year = Column(Integer)
    overview = Column(Text)
    mpaa_rating = Column(String(255))
    runtime_minutes = Column(Integer)
