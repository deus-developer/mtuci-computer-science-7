from abc import ABC

import psycopg2


class BaseRepository(ABC):
    def __init__(self, connection: "psycopg2.connection"):
        self._connection = connection

    def commit(self):
        pass

    def rollback(self):
        pass
