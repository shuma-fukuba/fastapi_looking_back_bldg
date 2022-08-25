import os
import datetime
from os.path import join, dirname, abspath
import pandas as pd
import numpy as np
from uuid import uuid4
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from database import SessionLocal
from models import User, PosseYear, InputCurriculum, OutputCurriculum

COLOR_GREEN = '\033[92m'
COLOR_END = '\033[0m'

ROOT_DIR = dirname(abspath(__file__))
STATIC_URL = os.environ.get('STATIC_URL')
STATIC_PATH = join(ROOT_DIR,
                   '..', '..', '..',
                   'htdocs')
FILE_SEED_USERS = 'users.csv'
FILE_SEED_YEARS = 'posse_years.csv'


class Seeder:
    def __init__(self) -> None:
        self.db: Session = SessionLocal()
        self.df_users = pd.read_csv(join(ROOT_DIR,
                                         FILE_SEED_USERS))
        self.df_posse_years = pd.read_csv(join(ROOT_DIR,
                                               FILE_SEED_YEARS))
        self.df_users = self.__convert_nan_None(self.df_users)
        self.df_posse_years = self.__convert_nan_None(self.df_posse_years)

        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def seed(self):
        self.create_users()
        self.create_associations()
        self.db.commit()

    def create_users(self, commit: bool = True):
        self.create_posse_years()

        for idx, row in self.df_users.iterrows():
            print(f'{COLOR_GREEN}{idx}/{len(self.df_users)} {COLOR_END}')
            uuid = uuid4()
            username = row.username
            email = row.email
            hashed_password = self.pwd_context.hash(row.password)
            university = row.university
            university_entrance_year = row.university_entrance_year
            expected_university_graduation_year = row.expected_university_graduation_year

            posse_year = self.db.query(PosseYear).filter(
                PosseYear.year == row.student_in_year_of_posse).one_or_none()

            posse_year_id = posse_year.uuid

            obj = {
                'uuid': uuid,
                'email': email,
                'hashed_password': hashed_password,
                'username': username,
                'posse_year_id': posse_year_id,
                'university': university,
                'university_entrance_year': university_entrance_year,
                'expected_university_graduation_year': expected_university_graduation_year,
            }

            user = User(**obj)
            self.db.add(user)

        if commit:
            try:
                self.db.commit()
            except Exception:
                self.db.rollback()

    def create_posse_years(self, commit: bool = True):
        for idx, row in self.df_posse_years.iterrows():
            year = row.year
            entrance_date = row.entrance_date

            entrance_date = datetime.datetime.strptime(
                entrance_date, '%Y/%m/%d')
            entrance_date = datetime.date(
                entrance_date.year,
                entrance_date.month,
                entrance_date.day)

            obj = {
                'year': year,
                'entrance_date': entrance_date,
            }

            posse_year = PosseYear(**obj)
            self.db.add(posse_year)

        if commit:
            try:
                self.db.commit()
            except Exception:
                self.db.rollback()

    def create_associations(self, commit: bool = False):
        print(f'{COLOR_GREEN} Seeding associations {COLOR_END}')
        users = self.db.query(User).all()
        input_curriculums = self.db.query(InputCurriculum).all()
        output_curriculums = self.db.query(OutputCurriculum).all()

        if not input_curriculums:
            raise Exception

        if not output_curriculums:
            raise Exception

        for user in users:
            current_input = user.input_curriculums
            current_output = user.output_curriculums
            input_curriculums.extend(current_input)
            output_curriculums.extend(current_output)

            user.input_curriculums = [c for c in input_curriculums]
            user.output_curriculums = [c for c in output_curriculums]

        if commit:
            try:
                self.db.commit()
            except Exception:
                self.db.rollback()

    def __convert_nan_None(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.replace([np.nan], [None])


if __name__ == '__main__':
    seeder = Seeder()
    seeder.seed()
