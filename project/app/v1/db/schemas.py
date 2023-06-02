from pydantic import BaseModel


class SubscriberBase(BaseModel):
    email: str

class Subscriber(SubscriberBase):
    sub_id: int

    class Config:
        orm_mode = True
