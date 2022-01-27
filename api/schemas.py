from pydantic import BaseModel


class MovieBase(BaseModel):
    title: str | None = None
    release_year: int | None = None
    overview: str | None = None
    mpaa_rating: str | None = None
    runtime_minutes: int | None = None

    class Config:
        orm_mode = True


class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True
