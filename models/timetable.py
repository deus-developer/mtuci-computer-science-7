import datetime
from dataclasses import dataclass


@dataclass
class TimeTable:
    subject_name: str
    teacher_full_name: str
    audience: str

    date: datetime.datetime
