from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models import MyCollDeclarativeBase


# https://towardsdatascience.com/a-guide-on-how-to-interact-between-python-and-databases-using-sqlalchemy-and-postgresql-a6d770723474

DATABASE_URL = "postgresql://mycoll:key_to_the_kingdom@localhost:5432/mycoll"

engine = create_engine(DATABASE_URL, future=True)
MyCollDeclarativeBase.metadata.create_all(engine)
print('applying models: success')
