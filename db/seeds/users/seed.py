import os
from os.path import join, dirname, abspath
import pandas as pd
import numpy as np
from uuid import uuid4

from database import SessionLocal
from models import User

COLOR_GREEN = '\033[92m'
COLOR_END = '\033[0m'

ROOT_DIR = dirname(abspath(__file__))
STATIC_URL = os.environ.get('STATIC_URL')
STATIC_PATH = join(ROOT_DIR,
                   '..', '..', '..',
                   'htdocs')
FILE_SEED_USERS = 'users.csv'


class Seeder:
    def __init__(self) -> None:
        self.db = SessionLocal()
        self.df_users = pd.read_csv(join(ROOT_DIR,
                                         FILE_SEED_USERS))
        self.df_users = self.__convert_nan_None(self.df_users)

    def seed(self):
        self.create_users()
        self.db.commit()

    def create_users(self, commit: bool = False):
        for idx, row in self.df_users.iterrows():
            print(f'{COLOR_GREEN}{idx}/{len(self.df_users)} {COLOR_END}')
            uuid = uuid4()
            username = row.username
            # TODO cognito_user_id must be in cognito userpool
            cognito_user_id = uuid4()
            student_in_year_of_posse = row.student_in_year_of_posse
            university = row.university
            university_entrance_year = row.university_entrance_year
            expected_university_graduation_year = row.expected_university_graduation_year

            obj = {
                'uuid': uuid,
                'cognito_user_id': cognito_user_id,
                'username': username,
                'student_in_year_of_posse': student_in_year_of_posse,
                'university': university,
                'university_entrance_year': university_entrance_year,
                'expected_university_graduation_year': expected_university_graduation_year,
            }

            user = User(**obj)
            self.db.add(user)

        if commit:
            self.db.commit()

    def __convert_nan_None(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.replace([np.nan], [None])


if __name__ == '__main__':
    seeder = Seeder()
    seeder.seed()
