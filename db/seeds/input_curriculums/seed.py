import os
from uuid import uuid4
from os.path import join, dirname, abspath
import pandas as pd
import numpy as np
from sqlalchemy.orm import Session
from sqlalchemy.exc import StatementError

from database import SessionLocal
from models import InputCurriculum, Week

COLOR_GREEN = '\033[92m'
COLOR_END = '\033[0m'

ROOT_DIR = dirname(abspath(__file__))
STATIC_URL = os.environ.get('STATIC_URL')
STATIC_PATH = join(ROOT_DIR,
                   '..', '..', '..',
                   'htdocs')
FILE_SEED_INPUTS = 'input_curriculums.csv'


class Seeder:
    def __init__(self):
        self.db: Session = SessionLocal()
        self.df_input_curriculums = pd.read_csv(join(ROOT_DIR,
                                                     FILE_SEED_INPUTS), encoding='shift-jis',
                                                sep=',')
        self.df_input_curriculums = self.__convert_nan_None(
            self.df_input_curriculums)

    def seed(self):
        self.create_input_curriculums()
        self.db.commit()

    def create_input_curriculums(self, commit: bool = False):
        def get_week_id(week: int, model=Week):
            try:
                item = self.db.query(model).filter(
                    Week.week == week).one_or_none()
            except StatementError:
                pass
            if item is None:
                raise ValueError('invalid id given')
            return item.uuid

        for idx, row in self.df_input_curriculums.iterrows():
            print(f"{COLOR_GREEN}{idx}/{len(self.df_input_curriculums)} {COLOR_END}")
            uuid = uuid4()
            curriculum = row.curriculum
            week_id = get_week_id(row.week)
            obj = {
                'uuid': uuid,
                'curriculum_name': curriculum,
                'week_id': week_id
            }

            input_curriculum = InputCurriculum(**obj)
            self.db.add(input_curriculum)

        if commit:
            self.db.commit()

    def __convert_nan_None(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.replace([np.nan], [None])


if __name__ == '__main__':
    seeder = Seeder()
    seeder.seed()
