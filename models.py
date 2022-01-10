from sqlalchemy import Column, Integer, Text, String

# from somewhere import instantiated_declaractive_base


# This needs to inherit from the instantiated declarative base
class Movie():
    __tablename__ = "Movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    release_year = Column(Integer)
    overview = Column(Text)
    mpaa_rating = Column(String(255))
    runtime_minutes = Column(Integer)
    image_link = Column(String)
    tmdb_page_link = Column(String)
