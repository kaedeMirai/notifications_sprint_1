from apscheduler.schedulers.asyncio import AsyncIOScheduler

from util.scheduler.jobs import monthly_messages
from fastapi.logger import logger


class Scheduler:
    scheduler = AsyncIOScheduler()

    def start(self):
        logger.info("Setup scheduled jobs")
        # For testing you can use this:
        # self.scheduler.add_job(monthly_messages, trigger="interval", minutes=1)
        self.scheduler.add_job(monthly_messages, trigger="cron", year="*", month="*", day="last")
        self.scheduler.start()

    def stop(self):
        self.scheduler.shutdown()


scheduler = Scheduler()
