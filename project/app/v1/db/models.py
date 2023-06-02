from sqlalchemy import Column, Integer, String,  DateTime
from sqlalchemy.orm import declarative_mixin

from datetime import datetime
from .config import Base


@declarative_mixin
class Timestamp:
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.now, default=datetime.utcnow)

# Parrent
class Subscriber(Timestamp, Base):

    __tablename__ = "subscriber_list"

    sub_id = Column(Integer, primary_key=True)
    email = Column(String)


