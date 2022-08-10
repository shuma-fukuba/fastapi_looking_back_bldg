import uuid as uid
from database import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy_utils import UUIDType
from sqlalchemy.orm import relationship

from .mixins import TimestampMixin


class LearningTime(Base, TimestampMixin):
    __tablename__ = 'learning_times'

    uuid = Column(UUIDType(binary=False),
                  primary_key=True, default=uid.uuid4)

    learning_time = Column(Integer, nullable=False)

    """
    relationship
    """

    week = relationship("Week", back_populates='learning_times')

    week_id = Column(UUIDType(binary=False),
                     ForeignKey('weeks.uuid'),
                     nullable=False)

    user = relationship("User", back_populates='learning_times')

    user_id = Column(UUIDType(binary=False),
                     ForeignKey('users.uuid'),
                     nullable=False)
