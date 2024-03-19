from abc import ABC, abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    async def processing_notification(self, notification):
        pass

    @abstractmethod
    async def send_notification(self, to_email, subject, body):
        pass

    @abstractmethod
    async def save_to_database(self, to_email, subject, body):
        pass
