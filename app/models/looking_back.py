import uuid as uid
from database import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
from .mixins import TimestampMixin


class LookingBack(Base, TimestampMixin):
    __tablename__ = 'looking_backs'

    uuid = Column(UUIDType(binary=False), primary_key=True,
                  default=uid.uuid4)

    good_point = Column(String(256), nullable=False)
    why_it_worked = Column(String(256), nullable=False)
    should_continue = Column(String(256), nullable=False)
    bad_point = Column(String(256), nullable=False)
    why_it_didnt_worked = Column(String(256), nullable=False)
    should_stop = Column(String(256), nullable=False)
    improve_point = Column(String(256), nullable=False)

    '''
    relationships
    '''

    # looking_back belong to users many-to-one
    user = relationship("User", back_populates='looking_backs')
    user_id = Column(
        UUIDType(binary=False),
        ForeignKey('users.uuid'),
        nullable=False)

    # looking_back belongs to weeks many-to-one
    week = relationship("Week", back_populates='looking_backs')
    week_id = Column(
        UUIDType(binary=False),
        ForeignKey('weeks.uuid'),
        nullable=False)
