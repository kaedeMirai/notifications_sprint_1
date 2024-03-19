import uvicorn
import logging
from fastapi import FastAPI
from fastapi.logger import logger
from fastapi.responses import ORJSONResponse
from contextlib import asynccontextmanager

from api.v1.routers.router import router
from db.mongo import close_mongo_client
from util.db_util.mongo_init import init_notifications_db
from db.rmq import producer

from util.scheduler.scheduler import scheduler


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_notifications_db()
    await producer.connect_broker()
    await producer.create_queues()
    yield
    close_mongo_client()
    await producer.close()


def build_app():

    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())
    logger.info("Starting App")

    api_app = FastAPI(
        title="Notifications API",
        description="Send notifications with Notifications API",
        version="1.0.0",
        docs_url="/api/openapi",
        openapi_url="/api/openapi.json",
        default_response_class=ORJSONResponse,
        lifespan=lifespan
    )

    api_app.include_router(router, prefix="/api/v1")
    scheduler.start()

    return api_app


app = build_app()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8338,
        reload=True
    )
