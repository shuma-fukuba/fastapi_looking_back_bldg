from email.policy import default
from database import Base
from ..mixins import TimestampMixin
from sqlalchemy import Column, ForeignKey, Boolean
from sqlalchemy_utils import UUIDType


class UsersInputCurriculums(Base, TimestampMixin):
    __tablename__ = 'users_input_curriculums'

    done = Column(
        Boolean,
        nullable=False,
        default=False
    )

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
