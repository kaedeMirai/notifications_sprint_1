from motor.motor_asyncio import AsyncIOMotorClient
from core.settings import settings

client: AsyncIOMotorClient = AsyncIOMotorClient(settings.mongo_conn)


def get_mongo_client():
    return client


def close_mongo_client():
    client.close()
