import logging

from sender.base_sender import BaseProvider

logger = logging.getLogger(__name__)


class SMSProvider(BaseProvider):

    async def processing_notification(self, notification):
        # Additional notification processing
        pass

    async def send_notification(self, recipient, subject, body):
        # Logic of sending SMS notifications
        logger.info('The SMS was sent successfully.')

    async def save_to_database(self, notification):
        pass
