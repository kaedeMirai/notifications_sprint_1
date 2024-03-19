from pydantic import Field
from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    smtp_host: str = Field(alias="SMTP_HOST")
    smtp_port: str = Field(alias="SMTP_PORT")
    gmail_password: str = Field(alias="GMAIL_PASSWORD")
    gmail_username: str = Field(alias="GMAIL_USERNAME")

    rabbit_url: str = Field(alias='RABBIT_URL')
    queues_rabbit: list = Field(alias='QUEUES_RABBIT')
    mongo_url: str = Field(alias='MONGO_URL')
    mongo_db: str = Field(alias='MONGO_DB')
    mongo_collection: str = Field(alias='MONGO_COLLECTION')

    class Config:
        env_file = "../../.env"


settings = Setting()
