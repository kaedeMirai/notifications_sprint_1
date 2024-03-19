from fastapi import APIRouter, Depends
from fastapi import HTTPException, status

from api.v1.schemas.schemas import DistributionDto
from services.notifications_service import get_notifications_service, NotificationsService

router = APIRouter(prefix="/notifications", tags=["notifications"])


@router.post(
    "/notify",
    summary="Notify users",
    description="Notify users",
    response_model=dict
)
async def notify(
        distribution_data: DistributionDto,
        service: NotificationsService = Depends(get_notifications_service)
):
    try:
        await service.notify(distribution_data)
        return {"detail": "Notification successfully created"}
    except Exception as e:
        raise HTTPException(
            detail=str(e),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@router.get(
    "/get_history",
    summary="Get notifications history",
    description="Get notifications history",
    response_model=dict
)
async def get_history(
        user_id: str,
        service: NotificationsService = Depends(get_notifications_service)
):
    try:
        history = await service.get_history(user_id)
        return {"detail": history}
    except Exception as e:
        raise HTTPException(
            detail=str(e),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


"""
REQUESTS BODY EXAMPLES:
    1. user_registered
    {
        "notification_id": "user_registered",
        "payload": {"user_id": "1"}
    }
    
    2. new_episode
    {
        "notification_id": "new_episode",
        "payload": {"movie_id": "1", "expiration_date":"22-01-2024"}
    }
    
    3. most_viewed_movies
    {
        "notification_id": "most_viewed_movies",
        "payload": {"expiration_date":"22-01-2024"}
    }
    
    4. custom_distribution
    {
        "notification_id": "custom_distribution",
        "payload": {
            "message": "<b>Hi, how are you?</b>",
            "group_id": 1234567,
            "channel": "tg",
            "expiration_date":"22-01-2024"
        }
    }
"""
