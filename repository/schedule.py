import datetime
from typing import List, Tuple, Any

from models import TimeTable
from .base import BaseRepository

GET_SCHEDULE_BY_WEEK_SQL = """
select
    "subject"."name",
    "teacher"."full_name",
    "timetable"."room_numb",
    "timetable"."day",
    "timetable"."start_time"
from
    "timetable"
join "subject" on
    "subject"."name" = "timetable"."subject"
left outer join teacher on
    "teacher"."subject" = "subject"."name"
where
    "timetable"."day" in %s
"""

GET_SCHEDULE_BY_DAY_SQL = """
select
    "subject"."name",
    "teacher"."full_name",
    "timetable"."room_numb",
    "timetable"."day",
    "timetable"."start_time"
from
    "timetable"
join "subject" on
    "subject"."name" = "timetable"."subject"
left outer join teacher on
    "teacher"."subject" = "subject"."name"
where
    "timetable"."day" = (%s)
order by
    "timetable"."day",
    "timetable"."start_time"
"""


def get_schedule_from_tuple(
    start_schedule_week_date: datetime.datetime, row: Tuple[Any, ...]
) -> TimeTable:
    subject_name, teacher_full_name, audience_number, day, start_time = row

    hour, minute = divmod(start_time, 60)
    date = start_schedule_week_date + datetime.timedelta(
        days=day - 1, hours=hour, minutes=minute
    )

    return TimeTable(
        subject_name=subject_name,
        teacher_full_name=teacher_full_name or "-",
        audience=audience_number,
        date=date,
    )


class ScheduleRepository(BaseRepository):
    def get_schedule_by_days(
        self, start_schedule_week_date: datetime.datetime, schedule_days: List[int]
    ) -> List[TimeTable]:
        result: List[TimeTable] = []

        with self._connection.cursor() as cursor:
            cursor.execute(GET_SCHEDULE_BY_WEEK_SQL, (tuple(schedule_days),))

            for row in cursor.fetchall():
                result.append(get_schedule_from_tuple(start_schedule_week_date, row))

        return result

    def get_schedule_by_day(
        self, start_schedule_week_date: datetime.datetime, schedule_day: int
    ) -> List[TimeTable]:
        result: List[TimeTable] = []

        with self._connection.cursor() as cursor:
            cursor.execute(GET_SCHEDULE_BY_DAY_SQL, (schedule_day,))

            for row in cursor.fetchall():
                result.append(get_schedule_from_tuple(start_schedule_week_date, row))

        return result
