from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


# https://towardsdatascience.com/a-guide-on-how-to-interact-between-python-and-databases-using-sqlalchemy-and-postgresql-a6d770723474
# The address uses "db" here instead of "localhost" because "db" refers back
# to the container that docker-compose created to run that service within
DATABASE_URL = "postgresql://mycoll:key_to_the_kingdom@db:5432/mycoll"

engine = create_engine(DATABASE_URL, future=True)
SessionLocal = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
