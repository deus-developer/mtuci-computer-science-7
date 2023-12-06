import psycopg2

from .base import BaseRepository
from .schedule import ScheduleRepository


class Repository(BaseRepository):
    def __init__(self, connection: "psycopg2.connection"):
        super().__init__(connection)

        self.schedule = ScheduleRepository(self._connection)
