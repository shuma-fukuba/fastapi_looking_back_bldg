import os
from os.path import join, dirname, abspath
import pandas as pd
import numpy as np
from uuid import uuid4

from database import SessionLocal
from models import Week

COLOR_GREEN = '\033[92m'
COLOR_END = '\033[0m'

ROOT_DIR = dirname(abspath(__file__))
STATIC_URL = os.environ.get('STATIC_URL')
STATIC_PATH = join(ROOT_DIR,
                   '..', '..', '..',
                   'htdocs')
FILE_SEED_WEEKS = 'weeks.csv'


class Seeder:
    def __init__(self) -> None:
        self.db = SessionLocal()
        self.df_weeks = pd.read_csv(join(ROOT_DIR,
                                         FILE_SEED_WEEKS))
        self.df_weeks = self.__convert_nan_None(self.df_weeks)

    def seed(self):
        self.create_weeks()
        self.db.commit()

    def create_weeks(self, commit: bool = False):
        for idx, row in self.df_weeks.iterrows():
            print(f"{COLOR_GREEN}{idx}/{len(self.df_weeks)} {COLOR_END}")
            uuid = uuid4()
            week = int(row.week)
            obj = {
                'uuid': uuid,
                'week': week
            }
            # print(obj)
            new_week = Week(**obj)
            self.db.add(new_week)

        if commit:
            self.db.commit()

    def __convert_nan_None(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.replace([np.nan], [None])


if __name__ == "__main__":
    seeder = Seeder()
    seeder.seed()
