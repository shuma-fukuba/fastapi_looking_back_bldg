import uuid as uid
from database import Base
from sqlalchemy import Column, Integer
from sqlalchemy_utils import UUIDType
from sqlalchemy.orm import relationship

from .mixins import TimestampMixin


class Week(Base, TimestampMixin):
    __tablename__ = 'weeks'

    uuid = Column(UUIDType(binary=False),
                  primary_key=True, default=uid.uuid4)

    week = Column(Integer, nullable=False, unique=True)

    """
    relationships
    """
    # week hasMany looking_backes one-to-many
    looking_backs = relationship('LookingBack', back_populates='week')
    learning_times = relationship("LearningTime", back_populates='week')
    input_curriculums = relationship("InputCurriculum", back_populates='week')
    output_curriculums = relationship(
        "OutputCurriculum", back_populates='week')
