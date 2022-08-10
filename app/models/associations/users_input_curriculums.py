from database import Base
from ..mixins import TimestampMixin
from sqlalchemy import Column, ForeignKey
from sqlalchemy_utils import UUIDType


class UsersInputCurriculums(Base, TimestampMixin):
    __tablename__ = 'users_input_curriculums'

    user_id = Column(
        UUIDType(binary=False),
        ForeignKey('users.uuid'),
        primary_key=True
    )

    input_curriculum_id = Column(
        UUIDType(binary=False),
        ForeignKey('input_curriculums.uuid'),
        primary_key=True
    )
