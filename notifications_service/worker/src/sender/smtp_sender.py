import logging
from datetime import datetime

import aiosmtplib
from email.message import EmailMessage
from motor.motor_asyncio import AsyncIOMotorClient

from core.config import settings
from sender.base_sender import BaseProvider

logger = logging.getLogger(__name__)


class SMTPProvider(BaseProvider):
    def __init__(self, smtp_host, smtp_port, username, password, mongo_url):
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
        self.mongo_url = mongo_url

        self.db_client = AsyncIOMotorClient(self.mongo_url)
        self.db = self.db_client[settings.mongo_db]
        self.collection = self.db[settings.mongo_url]

    async def processing_notification(self, notification):
        pass

    async def send_notification(self, to_email, subject, body):
        message = EmailMessage()
        message['From'] = self.username
        message['To'] = to_email
        message['Subject'] = subject
        message.set_content(body)
        await self.save_to_database(to_email, subject, body)
        try:
            # real smtp server
            # async with aiosmtplib.SMTP(
            #         hostname=self.smtp_host,
            #         port=self.smtp_port,
            #         username=self.username,
            #         password=self.password,
            #         use_tls=True
            #         ) as smtp:
            # mailhog, fake smtp server for test.
            async with aiosmtplib.SMTP(
                    hostname='mailhog',
                    port=1025,
                    ) as smtp:
                await smtp.send_message(message)
                logger.info('The email was sent successfully.')
        except Exception as ex:
            logger.error(f'Error: {ex}')

    async def save_to_database(self, to_email, subject, body):
        await self.collection.insert_one({
            "to_email": to_email,
            "subject": subject,
            "body": body,
            "timestamp": datetime.utcnow()
        })
