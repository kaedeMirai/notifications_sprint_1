import uuid
import httpx
import json

from models.users import BaseUser
from models.movies import BaseMovieDto, MostViewedMoviesDto


async def get_user_data(user_id: str) -> BaseUser:
    """Mock retrieving actual data"""

    response = httpx.get(f"http://mock_data_api_service:8000/api/v1/mock_data/get_user_data?user_id={user_id}")
    return BaseUser(**response.json())


async def get_group_data(group_id: str):
    """Mock retrieving actual data"""

    response = httpx.get(f"http://mock_data_api_service:8000/api/v1/mock_data/get_group_data?group_id={group_id}")
    users_data = response.json()
    return [BaseUser(**user) for user in users_data]


async def get_subscribed_users_data() -> list[BaseUser]:
    """Mock retrieving actual data"""

    response = httpx.get(f"http://mock_data_api_service:8000/api/v1/mock_data/get_subscribed_users_data")
    users_data = response.json()
    return [BaseUser(**user) for user in users_data]


async def get_most_viewed_movies_data(user_id: str) -> MostViewedMoviesDto:
    """Mock retrieving actual data"""

    response = httpx.get(
        f"http://mock_data_api_service:8000/api/v1/mock_data/get_most_viewed_movies_data?user_id={user_id}"
    )
    return MostViewedMoviesDto(**response.json())


async def get_movie_data(movie_id: str) -> BaseMovieDto:
    """Mock retrieving actual data"""

    response = httpx.get(f"http://mock_data_api_service:8000/api/v1/mock_data/get_movie_data?movie_id={movie_id}")
    return BaseMovieDto(**response.json())
