import datetime
import math


class Week:

    @classmethod
    def get_this_week(cls, old_day: datetime.date,
                      today: datetime = datetime.datetime.today().date()) -> int:
        td = today - old_day
        return math.floor(td.days / 7)

    @classmethod
    def get_curriculum_in_this_week():
        pass
