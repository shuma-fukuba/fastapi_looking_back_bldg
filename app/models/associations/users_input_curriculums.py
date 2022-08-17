from database import Base
from ..mixins import TimestampMixin
from sqlalchemy import Column, ForeignKey, Boolean
from sqlalchemy.orm import relationship
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

    users = relationship('User', back_populates='users_input_curriculum')

    input_curriculums = relationship('InputCurriculum', back_populates='users_input_curriculum')
