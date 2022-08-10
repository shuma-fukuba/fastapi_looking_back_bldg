import uuid as uid
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType

from database import Base
from .mixins import TimestampMixin
from .associations.users_input_curriculums import UsersInputCurriculums
from .associations.users_output_curriculums import UsersOutputCurriculums


class CurriculumBase(Base, TimestampMixin):
    __abstract__ = True
    uuid = Column(UUIDType(binary=False),
                  primary_key=True,
                  default=uid.uuid4)

    curriculum_name = Column(String(256), nullable=False)


class InputCurriculum(CurriculumBase):
    __tablename__ = 'input_curriculums'

    '''
    relationships
    '''

    users = relationship(
        'User',
        secondary=UsersInputCurriculums.__tablename__,
        back_populates='input_curriculums'
    )


class OutputCurriculum(CurriculumBase):
    __tablename__ = 'output_curriculums'

    '''
    relationships
    '''
    # 中間テーブルが生成されるように
    users = relationship(
        'User',
        secondary=UsersOutputCurriculums.__tablename__,
        back_populates='output_curriculums'
    )
