import datetime
from typing import List

start_schedule_date = datetime.datetime(year=2023, month=9, day=1)


def is_second_week(date: datetime.datetime) -> bool:
    isocalendar = date.isocalendar()
    return isocalendar.week % 2 == 0


def get_schedule_day(date: datetime.datetime) -> int:
    isocalendar = date.isocalendar()

    if isocalendar.week % 2:
        return isocalendar.weekday
    return isocalendar.weekday + 7


def get_start_schedule_week_date(date: datetime.datetime) -> datetime.datetime:
    start_week_date = date - datetime.timedelta(days=date.weekday())
    if is_second_week(date):
        start_week_date -= datetime.timedelta(days=7)

    return start_week_date.replace(hour=0, minute=0, second=0, microsecond=0)


def get_week_range_schedule(start_week_date: datetime.datetime) -> List[int]:
    result: List[int] = []
    for weekday in range(7):
        result.append(
            get_schedule_day(start_week_date + datetime.timedelta(days=weekday))
        )

    return result


WEEKDAYS: List[str] = [
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье",
]


def get_weekday_name(weekday: int) -> str:
    return WEEKDAYS[weekday - 1]


def get_week_day_label(date: datetime.date) -> str:
    weekday_name = get_weekday_name(date.isoweekday())

    return (
        f"{weekday_name.capitalize()} – {date.day:02d}.{date.month:02d}.{date.year:02d}"
    )
