import json
import logging

import aio_pika

from core.config import settings

logger = logging.getLogger(__name__)


async def consumer(queue_name, smtp_provider, sms_provider, telegram_provider):
    connection = await aio_pika.connect_robust(settings.rabbit_url)
    channel = await connection.channel()
    queue = await channel.declare_queue(queue_name, durable=True)

    async with queue.iterator() as queue_iter:
        async for message in queue_iter:
            try:
                notification = json.loads(message.body.decode("utf-8"))
            except json.JSONDecodeError:
                logging.error("Invalid JSON message: %s", message.body.decode("utf-8"))
                continue
            try:
                channel_type = notification.get('channel')
                if channel_type == 'sms':
                    provider = sms_provider
                elif channel_type == 'tg':
                    provider = telegram_provider
                elif channel_type == 'email':
                    provider = smtp_provider

                await provider.processing_notification(notification)
                await provider.send_notification(
                    notification['recipient'],
                    notification.get('subject', ''),
                    notification['body']
                    )
                await message.ack()
            except Exception as e:
                logging.error("Error processing or sending email: %s", str(e))
                await message.nack()
