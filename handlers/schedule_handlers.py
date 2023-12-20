import datetime
import html
from collections import defaultdict
from typing import List, Tuple, Dict

from telebot import TeleBot
from telebot.types import Message

from models import TimeTable
from repository import Repository
from utils import (
    get_start_schedule_week_date,
    get_week_range_schedule,
    get_week_day_label,
    is_second_week,
    get_weekday_name,
)

SUBJECT_TEXT_TEMPLATE = (
    "<b>{subject_name}</b>\n"
    "Аудитория: {audience_number}\n"
    "Время: {hour:02d}:{minute:02d}\n"
    "Преподаватель: {teacher_full_name}"
)
WEEK_DAY_SCHEDULE_TEXT_TEMPLATE = "<b>{weekday_label}</b>\n" "{day_subjects_text}"
WEEK_SCHEDULE_TEXT_TEMPLATE = "<b>{week_caption}</b>\n\n" "{week_subjects_text}"
SCHEDULE_TEXT_TEMPLATE = "<b>РАСПИСАНИЕ НА {schedule_label}</b>\n\n" "{schedule_text}"


def get_schedule_text_by_date(timetables: List[TimeTable]) -> str:
    day_subjects_chunks: List[str] = []
    for timetable in timetables:
        day_subjects_chunks.append(
            SUBJECT_TEXT_TEMPLATE.format(
                subject_name=html.escape(timetable.subject_name),
                audience_number=timetable.audience or "-",
                hour=timetable.date.hour,
                minute=timetable.date.minute,
                teacher_full_name=html.escape(timetable.teacher_full_name),
            )
        )

    text = "\n\n".join(day_subjects_chunks)
    return text


def get_sorted_schedule_by_week(
    schedule: List[TimeTable],
) -> List[Tuple[datetime.date, List[TimeTable]]]:
    schedule.sort(key=lambda t: t.date)

    schedule_by_date: Dict[datetime.date, List[TimeTable]] = defaultdict(list)
    for timetable in schedule:
        schedule_by_date[timetable.date.date()].append(timetable)

    result: List[Tuple[datetime.date, List[TimeTable]]] = []
    for schedule_date in sorted(schedule_by_date.keys()):
        result.append((schedule_date, schedule_by_date[schedule_date]))

    return result


def week_schedule_handler(
    message: Message, bot: TeleBot, repository: Repository, is_current_week: bool
):
    date = datetime.datetime.fromtimestamp(message.date)
    weekday = date.weekday()
    start_week_date = date - datetime.timedelta(days=weekday)
    if not is_current_week:
        start_week_date += datetime.timedelta(weeks=1)

    schedule_days = get_week_range_schedule(start_week_date)

    start_schedule_week_date = get_start_schedule_week_date(date)
    schedule = repository.schedule.get_schedule_by_days(
        start_schedule_week_date=start_schedule_week_date, schedule_days=schedule_days
    )

    schedule_text = "\n\n".join(
        WEEK_DAY_SCHEDULE_TEXT_TEMPLATE.format(
            weekday_label=get_week_day_label(schedule_date),
            day_subjects_text=get_schedule_text_by_date(timetables),
        )
        for schedule_date, timetables in get_sorted_schedule_by_week(schedule)
    )

    schedule_label = "неделю" if is_current_week else "следующую неделю"

    text = SCHEDULE_TEXT_TEMPLATE.format(
        schedule_label=schedule_label.upper(), schedule_text=schedule_text
    )
    return bot.reply_to(message, text=text)


def day_schedule_handler(
    message: Message, bot: TeleBot, repository: Repository, weekday: int
):
    date = datetime.datetime.fromtimestamp(message.date)
    start_schedule_week_date = get_start_schedule_week_date(date)

    schedule_day = weekday
    if is_second_week(date):
        schedule_day += 7

    schedule = repository.schedule.get_schedule_by_day(
        start_schedule_week_date=start_schedule_week_date, schedule_day=schedule_day
    )

    schedule_text = get_schedule_text_by_date(schedule)
    weekday_name = get_weekday_name(weekday)

    text = SCHEDULE_TEXT_TEMPLATE.format(
        schedule_label=weekday_name.upper(), schedule_text=schedule_text
    )
    return bot.reply_to(message, text=text)
