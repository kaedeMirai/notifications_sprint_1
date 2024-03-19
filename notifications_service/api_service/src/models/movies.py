from pydantic import BaseModel


class BaseMovieDto(BaseModel):
    name: str


class MostViewedMoviesDto(BaseModel):
    movies_watched: int
    equal_category_movies: int
    category: str
