import json
from fastapi.encoders import jsonable_encoder
from aio_pika import connect, Message

from core.settings import settings


class RmqProducer:
    INSTANT_QUEUE = "instant"
    DEFERRED_QUEUE = "deferred"
    AVAILABLE_QUEUES = [INSTANT_QUEUE, DEFERRED_QUEUE]

    def __init__(self, dsn):
        self.dsn = dsn
        self.connection = None

    async def connect_broker(self):
        self.connection = await connect(self.dsn)

    async def close(self):
        await self.connection.close()

    async def create_queues(self):
        async with self.connection.channel() as channel:
            for queue in self.AVAILABLE_QUEUES:
                await channel.declare_queue(queue, durable=True)

    async def publish(self, message: dict, queue: str):
        encoded_message = jsonable_encoder(message)

        if queue not in self.AVAILABLE_QUEUES:
            return

        async with self.connection.channel() as channel:
            await channel.default_exchange.publish(
                Message(body=json.dumps(encoded_message).encode("utf-8")),
                routing_key=queue
            )


producer = RmqProducer(settings.rmq_conn)
