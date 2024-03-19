import datetime
from datetime import timedelta

from services.notifications_service import get_notifications_service
from api.v1.schemas.schemas import DistributionDto


async def monthly_messages():
    exp_date = datetime.datetime.now() + timedelta(days=2)
    distribution_data = DistributionDto(
        notification_id="most_viewed_movies",
        payload={"expiration_date": exp_date.strftime("%d-%m-%Y")}
    )
    service = get_notifications_service()
    await service.notify(distribution_data)
