from database import Base  # noqa: F401

from .curriculums import InputCurriculum, OutputCurriculum  # noqa: F401
from .learning_time import LearningTime  # noqa: F401
from .week import Week  # noqa: F401
from .looking_back import LookingBack  # noqa: F401
from .user import User  # noqa: F401
from .posse_year import PosseYear  # noqa: F401
from .associations.users_input_curriculums import UsersInputCurriculums  # noqa: F401
from .associations.users_output_curriculums import UsersOutputCurriculums  # noqa: F401
