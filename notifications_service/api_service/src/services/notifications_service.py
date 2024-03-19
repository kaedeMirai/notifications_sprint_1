from api.v1.schemas.schemas import DistributionDto
from db.rmq import producer as rmq_producer
from db.mongo import get_mongo_client
from models.notifications import HistoryRecordDto
from services.handlers.handlers import (
    BaseHandler,
    UserRegisteredHandler,
    NewEpisodeHandler,
    MostViewedMoviesHandler,
    CustomDistributionHandler
)
from fastapi.logger import logger

NOTIFICATION_ID_TO_HANDLER_MAPPING = {
    "user_registered": UserRegisteredHandler,
    "new_episode": NewEpisodeHandler,
    "most_viewed_movies": MostViewedMoviesHandler,
    "custom_distribution": CustomDistributionHandler
}


class NotificationsService:
    def __init__(self, producer, mongo_client):
        self.producer = producer
        self.mongo_client = mongo_client

    async def notify(self, distribution_data: DistributionDto) -> None:
        db = self.mongo_client.get_database("notifications_db")
        collection = db.get_collection("notifications")

        notification = await collection.find_one({
            "id": distribution_data.notification_id
        })

        history_collection = db.get_collection("history")
        handler = NOTIFICATION_ID_TO_HANDLER_MAPPING[
            notification["id"]
        ](self.producer, history_collection)  # type: BaseHandler

        logger.info(f"Create notification task with id: {distribution_data.notification_id}")
        await handler.create_notification_tasks(distribution_data)

    async def get_history(self, user_id: str) -> list[dict]:
        db = self.mongo_client.get_database("notifications_db")
        collection = db.get_collection("history")

        cursor = collection.find({
            "user_id": user_id,
            "status": "SENT"
        }).limit(100)

        return [HistoryRecordDto(**history_record).model_dump() async for history_record in cursor]


def get_notifications_service() -> NotificationsService:
    return NotificationsService(
        producer=rmq_producer,
        mongo_client=get_mongo_client()
    )
