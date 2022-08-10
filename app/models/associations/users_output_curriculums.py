from database import Base
from ..mixins import TimestampMixin
from sqlalchemy import Column, ForeignKey
from sqlalchemy_utils import UUIDType


class UsersOutputCurriculums(Base, TimestampMixin):
    __tablename__ = 'users_output_curriculums'

    user_id = Column(
        UUIDType(binary=False),
        ForeignKey('users.uuid'),
        primary_key=True)

    output_curriculum_id = Column(
        UUIDType(binary=False),
        ForeignKey('output_curriculums.uuid'),
        primary_key=True
    )
