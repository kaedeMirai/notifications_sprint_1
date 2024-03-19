import uuid
from abc import abstractmethod

from api.v1.schemas.schemas import DistributionDto
from util.templates_util import (
    build_registration_email,
    build_new_episode_email,
    build_most_viewed_movies_email
)
from util.data_fetching_util import (
    get_user_data,
    get_movie_data,
    get_most_viewed_movies_data,
    get_subscribed_users_data,
    get_group_data
)


class BaseHandler:
    CHANNEL_TO_USER_FIELD_MAPPING = {
        "email": "email",
        "sms": "phone",
        "tg": "tg"
    }

    def __init__(self, producer, collection):
        self.producer = producer
        self.collection = collection

    @abstractmethod
    async def create_notification_tasks(self, distribution_data: DistributionDto):
        raise NotImplementedError()

    async def publish_notification_tasks(self, notification_tasks: list[dict], queue: str):
        for task in notification_tasks:
            await self.producer.publish(task, queue)

            notification_history_record = task
            notification_history_record["status"] = "PUBLISHED"
            await self.add_notification_history(notification_history_record)

    async def add_notification_history(self, notification_history_record: dict):
        await self.collection.insert_one(notification_history_record)


class UserRegisteredHandler(BaseHandler):
    def __init__(self, producer, collection):
        super().__init__(producer, collection)

    async def create_notification_tasks(self, distribution_data: DistributionDto):
        user_data = await get_user_data(distribution_data.payload["user_id"])
        email = build_registration_email(user_data)

        tasks = [{
            "id": str(uuid.uuid4()),
            "user_id": user_data.user_id,
            "body": email,
            "recipient": user_data.email,
            "channel": "email",
        }]
        await self.publish_notification_tasks(tasks, self.producer.INSTANT_QUEUE)


class NewEpisodeHandler(BaseHandler):
    def __init__(self, producer, collection):
        super().__init__(producer, collection)

    async def create_notification_tasks(self, distribution_data: DistributionDto):
        users_data = await get_subscribed_users_data()
        movie_data = await get_movie_data(distribution_data.payload["movie_id"])

        tasks = []
        for user in users_data:
            email = build_new_episode_email(user, movie_data)
            tasks.append({
                "id": str(uuid.uuid4()),
                "user_id": user.user_id,
                "body": email,
                "recipient": user.email,
                "channel": "email",
                "expiration_date": distribution_data.payload["expiration_date"]
            })

        await self.publish_notification_tasks(tasks, self.producer.DEFERRED_QUEUE)


class MostViewedMoviesHandler(BaseHandler):
    def __init__(self, producer, collection):
        super().__init__(producer, collection)

    async def create_notification_tasks(self, distribution_data: DistributionDto):
        users_data = await get_subscribed_users_data()

        tasks = []
        for user in users_data:
            most_viewed_movies_data = await get_most_viewed_movies_data(user.user_id)
            email = build_most_viewed_movies_email(user, most_viewed_movies_data)
            tasks.append({
                "id": str(uuid.uuid4()),
                "user_id": user.user_id,
                "body": email,
                "recipient": user.email,
                "channel": "email",
                "expiration_date": distribution_data.payload["expiration_date"]
            })

        await self.publish_notification_tasks(tasks, self.producer.DEFERRED_QUEUE)


class CustomDistributionHandler(BaseHandler):
    def __init__(self, producer, collection):
        super().__init__(producer, collection)

    async def create_notification_tasks(self, distribution_data: DistributionDto):
        users_data = await get_group_data(distribution_data.payload["group_id"])

        tasks = []
        for user in users_data:
            body = distribution_data.payload["message"]
            channel = distribution_data.payload["channel"]
            tasks.append({
                "id": str(uuid.uuid4()),
                "user_id": user.user_id,
                "body": body,
                "recipient": user.model_dump()[self.CHANNEL_TO_USER_FIELD_MAPPING[channel]],
                "channel": channel,
                "expiration_date": distribution_data.payload["expiration_date"]
            })

        await self.publish_notification_tasks(tasks, self.producer.DEFERRED_QUEUE)
