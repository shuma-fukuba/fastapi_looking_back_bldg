import uuid as uid
from database import Base
from .mixins import TimestampMixin
from sqlalchemy import Integer, Column, String, ForeignKey
# from sqlalchemy.dialects.mysql import INTEGER, BIGINT, FLOAT
from sqlalchemy_utils import UUIDType
from sqlalchemy.orm import relationship

from .associations.users_input_curriculums import UsersInputCurriculums
from .associations.users_output_curriculums import UsersOutputCurriculums

# UnsignedInt = Integer().with_variant(INTEGER(unsigned=True), 'mysql')
# UnsignedBigInt = Integer().with_variant(BIGINT(unsigned=True), 'mysql')
# UnsignedFloat = Float().with_variant(FLOAT(unsigned=True), 'mysql')


class User(Base, TimestampMixin):
    __tablename__ = 'users'

    uuid = Column(UUIDType(binary=False),
                  primary_key=True, default=uid.uuid4)

    cognito_user_id = Column(UUIDType(binary=False),
                             unique=True)

    username = Column(String(256), unique=True, nullable=False)
    university = Column(String(256), nullable=True)
    university_entrance_year = Column(Integer, nullable=True)
    expected_university_graduation_year = Column(Integer, nullable=True)

    line_id = Column(String(256), nullable=True)

    github_username = Column(String(256), nullable=True)

    github_repository = Column(String(256), nullable=True)

    github_access_token = Column(String(256), nullable=True)

    '''
    relationships
    '''

    posse_year_id = Column(UUIDType(binary=False),
                           ForeignKey('posse_years.uuid'),
                           nullable=False)

    posse_year = relationship('PosseYear', back_populates='users')

    # user hasMany learning_times one-to-many
    learning_times = relationship("LearningTime", back_populates='user')

    looking_backs = relationship("LookingBack", back_populates='user')

    input_curriculums = relationship(
        'InputCurriculum',
        secondary=UsersInputCurriculums.__tablename__,
        back_populates='users'
    )

    output_curriculums = relationship(
        "OutputCurriculum",
        secondary=UsersOutputCurriculums.__tablename__,
        back_populates='users'
    )

    users_input_curriculum = relationship("UsersInputCurriculums", back_populates='users')

    users_output_curriculum = relationship("UsersOutputCurriculums", back_populates='users')
