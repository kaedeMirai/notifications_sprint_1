from pydantic import BaseModel


class DistributionDto(BaseModel):
    notification_id: str
    payload: dict
