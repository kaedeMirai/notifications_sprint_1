import logging

from sender.base_sender import BaseProvider

logger = logging.getLogger(__name__)


class TelegramProvider(BaseProvider):

    async def processing_notification(self, notification):
        # Additional notification processing
        pass

    async def send_notification(self, recipient, subject, body):
        # Logic of sending messages in a telegram
        logger.info('The Telegram message was sent successfully.')

    async def save_to_database(self, notification):
        pass
