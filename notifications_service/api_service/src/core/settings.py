from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mongo_conn: str = Field(default="mongodb://admin:admin@0.0.0.0:27023/", alias="MONGO_CONN")
    rmq_conn: str = Field(default="amqp://admin:admin@0.0.0.0:5672", alias="RMQ_CONN")


settings = Settings()
