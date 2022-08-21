import datetime
import math
from sqlalchemy.orm import Session
from sqlalchemy.exc import StatementError
from models import Week

from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST


class Week:

    @classmethod
    def get_this_week_num(cls, entrance_date: datetime.date,
                          today: datetime = datetime.datetime.today().date()) -> int:
        td = today - entrance_date
        return math.floor(td.days / 7)

    @classmethod
    def get_this_week_id(cls, db: Session,
                         model: Week,
                         entrance_date: datetime.date,
                         today: datetime.date = datetime.datetime.today().date()):
        this_week: int = cls.get_this_week_num(
            entrance_date=entrance_date, today=today)
        try:
            item = db.query(model).filter(
                model.week == this_week).one_or_none()
        except StatementError:
            pass

        if not item:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                                detail='this week could not found')
        return item.uuid

    @classmethod
    def get_this_week(cls, db: Session,
                      model: Week,
                      entrance_date: datetime.date,
                      today: datetime.date = datetime.datetime.today().date()):
        this_week_id = cls.get_this_week_id(
            db=db,
            model=model,
            entrance_date=entrance_date,
            today=today
        )
        try:
            item = db.query(model).get(this_week_id)
        except StatementError:
            pass

        if not item:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST,
                                detail='Invalid entrance date.')
        return item
