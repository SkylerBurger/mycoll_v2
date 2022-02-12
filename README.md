# MyColl v2

This project is a simple attempt at rebuilding a personal project in FastAPI to see how it differs from Django.

## Tools

|        Tool        | Function                              | Replaces from v1              |
|:------------------:|:--------------------------------------|-------------------------------|
|    **FastAPI**     | *Web Framework*                       | Django                        |
|         -          | *API Documentation*                   | Postman                       |
|    **Pydantic**    | *Data Validation & Serialization*     | djangorestframework           |
| **SQLAlchemy ORM** | *Object Relational Mapper*            | Django (Django ORM)           |
|    **Alembic**     | *Database Migration Management*       | Django                        |
|    **pgAdmin**     | *Database Management UI*              | Django                        |
|    **Psycopg2**    | *Implements Python's DBAPI*           | *same for both versions*      |
|   **PostgreSQL**   | *Database*                            | *same for both versions*      |
|    **Uvicorn**     | *Server*                              | gunicorn                      |
|    **Passlib**     | *Encryption (for passwords)*          | Django (auth)                 |
|  **Python-jose**   | *Creation and Interpretation of JWTs* | djangorestframework-simplejwt |
| **Python-dotenv**  | *Environment Variables Management*    | django-environ                |

## Resources

The following resources were referred to during this rebuild:

- [FastAPI - User Guide](https://fastapi.tiangolo.com/tutorial/)
- [YouTube - Tech with Tim - Python FastAPI Tutorial](https://www.youtube.com/watch?v=-ykeT6kk4bk)
- [YouTube - Bitfumes - FastAPI - A Python Framework | Full Course](https://www.youtube.com/watch?v=7t2alSnE2-I)
- [Compose - Using PostgreSQL through SQLAlchemy](https://www.compose.com/articles/using-postgresql-through-sqlalchemy/)
- [Alembic - Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
- [Alembic - Auto Generating Migrations](https://alembic.sqlalchemy.org/en/latest/autogenerate.html)
- [Towards Data Science - How to Run PostgreSQL and pgAdmin Using Docker](https://towardsdatascience.com/how-to-run-postgresql-and-pgadmin-using-docker-3a6a8ae918b5)
- [Pydantic - Usage - Schema](https://pydantic-docs.helpmanual.io/usage/schema/)