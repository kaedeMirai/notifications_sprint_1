from pydantic import BaseModel


class HistoryRecordDto(BaseModel):
    id: str
    user_id: str
    body: str
    recipient: str
    channel: str
    expiration_date: str
