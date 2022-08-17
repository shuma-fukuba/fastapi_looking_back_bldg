import datetime
import math
from sqlalchemy.orm import Session
from sqlalchemy.exc import StatementError
from models import Week

from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST
from schemas.week import ResponseWeekSchema


class Week:

    @classmethod
    def get_this_week(cls, entrance_date: datetime.date,
                      today: datetime = datetime.datetime.today().date()) -> int:
        td = today - entrance_date
        print(td)
        return math.floor(td.days / 7)

    @classmethod
    def get_this_week_id(cls, db: Session,
                         model: Week,
                         entrance_date: datetime.date,
                         today: datetime.date = datetime.datetime.today().date()):
        this_week: int = cls.get_this_week(entrance_date=entrance_date, today=today)
        try:
            item: ResponseWeekSchema = db.query(model).filter(
                model.week == this_week).one_or_none()
        except StatementError:
            pass

        if not item:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                                detail='this week could not found')
        return item.uuid

    @classmethod
    def get_curriculum_in_this_week():
        # TODO user_idから今週分のカリキュラムを取ってくる
        pass
