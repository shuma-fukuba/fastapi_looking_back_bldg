import os
from uuid import uuid4
from os.path import join, dirname, abspath
import pandas as pd
import numpy as np
from sqlalchemy.orm import Session
from sqlalchemy.exc import StatementError

from database import SessionLocal
from models import Week, InputCurriculum, OutputCurriculum
from models.curriculums import CurriculumBase

COLOR_GREEN = '\033[92m'
COLOR_END = '\033[0m'

ROOT_DIR = dirname(abspath(__file__))
STATIC_URL = os.environ.get('STATIC_URL')
STATIC_PATH = join(ROOT_DIR,
                   '..', '..', '..',
                   'htdocs')
FILE_SEED_INPUTS = 'input_curriculums.csv'
FILE_SEED_OUTPUTS = 'output_curriculums.csv'


class CurriculumSeederBase:
    def __init__(self):
        self.db: Session = SessionLocal()
        self.df_curriculums = None
        self.model = CurriculumBase

    def seed(self):
        self.create_curriculums()
        self.db.commit()

    def create_curriculums(self, commit: bool = False):
        def get_week_id(week: int, model=Week):
            try:
                item = self.db.query(model).filter(
                    Week.week == week).one_or_none()
            except StatementError:
                pass
            if item is None:
                raise ValueError('invalid id given')
            return item.uuid

        for idx, row in self.df_curriculums.iterrows():
            print(f"{COLOR_GREEN}{idx}/{len(self.df_curriculums)} {COLOR_END}")
            uuid = uuid4()
            curriculum = row.curriculum
            week_id = get_week_id(row.week)
            obj = {
                'uuid': uuid,
                'curriculum_name': curriculum,
                'week_id': week_id
            }

            item = self.model(**obj)
            self.db.add(item)

        if commit:
            self.db.commit()

    def convert_nan_None(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.replace([np.nan], [None])


class InputSeeder(CurriculumSeederBase):
    def __init__(self):
        super().__init__()
        self.df_curriculums = pd.read_csv(join(ROOT_DIR,
                                               FILE_SEED_INPUTS), encoding='shift-jis',
                                          sep=',')
        self.model = InputCurriculum
        self.df_curriculums = self.convert_nan_None(
            self.df_curriculums)


class OutputSeeder(CurriculumSeederBase):
    def __init__(self):
        super().__init__()
        self.df_curriculums = pd.read_csv(join(ROOT_DIR,
                                               FILE_SEED_OUTPUTS), encoding='shift-jis',
                                          sep=',')
        self.model = OutputCurriculum
        self.df_curriculums = self.convert_nan_None(
            self.df_curriculums)


if __name__ == "__main__":
    input_seeder = InputSeeder()
    input_seeder.seed()

    output_seeder = OutputSeeder()
    output_seeder.seed()
