import asyncio
import logging

from core.config import settings
from rabbit.consumer import consumer
from sender.sms_sender import SMSProvider
from sender.smtp_sender import SMTPProvider
from sender.telegram_sender import TelegramProvider


async def main():

    smtp_provider = SMTPProvider(
        smtp_host=settings.smtp_host,
        smtp_port=settings.smtp_port,
        username=settings.gmail_username,
        password=settings.gmail_password,
        mongo_url=settings.mongo_url
        )
    sms_provider = SMSProvider()
    telegram_provider = TelegramProvider()

    tasks = [consumer(queue, smtp_provider, sms_provider, telegram_provider)
             for queue in settings.queues_rabbit]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
