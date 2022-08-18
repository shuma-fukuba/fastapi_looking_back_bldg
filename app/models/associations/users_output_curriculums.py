from database import Base
from ..mixins import TimestampMixin
from sqlalchemy import Column, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType


class UsersOutputCurriculums(Base, TimestampMixin):
    __tablename__ = 'users_output_curriculums'

    done = Column(
        Boolean,
        nullable=False,
        default=False
    )

    user_id = Column(
        UUIDType(binary=False),
        ForeignKey('users.uuid'),
        primary_key=True)

    output_curriculum_id = Column(
        UUIDType(binary=False),
        ForeignKey('output_curriculums.uuid'),
        primary_key=True
    )

    users = relationship('User', back_populates='users_output_curriculum')
    output_curriculums = relationship('OutputCurriculum', back_populates='users_output_curriculum')
