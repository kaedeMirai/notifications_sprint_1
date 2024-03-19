from pydantic import BaseModel


class BaseUser(BaseModel):
    user_id: str
    first_name: str
    last_name: str
    email: str
    tg: str
    phone: str
