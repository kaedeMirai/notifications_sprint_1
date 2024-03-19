import uuid
import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.responses import ORJSONResponse
from random import randint

router = APIRouter(prefix="/mock_data", tags=["mock_data"])


@router.get(
    "/get_user_data",
    summary="Generate user data",
    description="Generate user data",
    response_model=dict
)
def generate_user_data(user_id: str):
    return generate_test_user_data(user_id)


@router.get(
    "/get_subscribed_users_data",
    summary="Generate subscribed users data",
    description="Generate subscribed users data",
    response_model=list[dict]
)
def generate_subscribed_users_data():
    users = [generate_user_data(str(uuid.uuid4())) for _ in range(500)]
    return users


@router.get(
    "/get_most_viewed_movies_data",
    summary="Generate most viewed movies data",
    description="Generate most viewed movies data",
    response_model=dict
)
def generate_most_viewed_movies_data(user_id: str):
    return {
        "movies_watched": randint(50, 150),
        "equal_category_movies": randint(1, 20),
        "category": f"Test {randint(1, 10)}"
    }


@router.get(
    "/get_movie_data",
    summary="Generate movie data",
    description="Generate movie data",
    response_model=dict
)
def generate_movie_data(movie_id: str):
    return {
        "name": f"Test {randint(1, 100)}"
    }


@router.get(
    "/get_group_data",
    summary="Generate users group data",
    description="Generate users group data",
    response_model=list[dict]
)
def generate_group_data(group_id: str):
    users = [generate_user_data(str(uuid.uuid4())) for _ in range(500)]
    return users


def generate_test_user_data(user_id):
    return {
        "user_id": user_id,
        "first_name": f"First {randint(1, 5000)}",
        "last_name": f"Last {randint(1, 5000)}",
        "email": f"test{randint(1, 5000)}@email.com",
        "tg": f"test{randint(1, 500)}",
        "phone": f"+{randint(1000000, 9999999)}"
    }


def build_app():
    api_app = FastAPI(
        title="Mock Data API",
        description="Generates mock data",
        version="1.0.0",
        docs_url="/api/openapi",
        openapi_url="/api/openapi.json",
        default_response_class=ORJSONResponse
    )

    api_app.include_router(router, prefix="/api/v1")

    return api_app


app = build_app()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8555,
        reload=True
    )
