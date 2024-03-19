from jinja2 import Environment, PackageLoader, select_autoescape

from models.users import BaseUser
from models.movies import BaseMovieDto, MostViewedMoviesDto

env = Environment(
    loader=PackageLoader("util"),
    autoescape=select_autoescape()
)


def build_registration_email(user_data: BaseUser):
    template = env.get_template("user_registered.html")
    return template.render(first_name=user_data.first_name, last_name=user_data.last_name)


def build_new_episode_email(user_data: BaseUser, movie_data: BaseMovieDto):
    template = env.get_template("new_episode.html")
    return template.render(
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        movie=movie_data.name
    )


def build_most_viewed_movies_email(user_data: BaseUser, movies_data: MostViewedMoviesDto):
    template = env.get_template("most_viewed_movies.html")
    return template.render(
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        movies_watched=movies_data.movies_watched,
        equal_category_movies=movies_data.equal_category_movies,
        category=movies_data.category
    )
