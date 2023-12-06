from typing import Set, Dict, Any, Optional

import psycopg2
from telebot import BaseMiddleware
from telebot.types import Message

from repository import Repository


class DatabaseMiddleware(BaseMiddleware):
    update_types: Set[str] = {
        "message",
    }

    def __init__(self, database_url: str):
        super().__init__()

        self.database_connection = psycopg2.connect(database_url)

    def pre_process(self, message: Message, data: Dict[str, Any]):
        data["repository"] = Repository(self.database_connection)

    def post_process(
        self, message: Message, data: Dict[str, Any], exception: Optional[Exception]
    ):
        pass
