import uuid as uid
from sqlalchemy import Column, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType

from database import Base
from .mixins import TimestampMixin


class PosseYear(Base, TimestampMixin):
    __tablename__ = 'posse_years'

    uuid = Column(UUIDType(binary=False),
                  primary_key=True, default=uid.uuid4)

    # 期生
    year = Column(Float, nullable=False, unique=True)

    # 入学した日
    entrance_date = Column(DateTime, nullable=False)

    '''
    relationships
    '''
    users = relationship('User', back_populates='posse_year')
