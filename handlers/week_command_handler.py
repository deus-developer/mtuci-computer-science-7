import datetime

from telebot import TeleBot
from telebot.types import Message

from repository import Repository
from utils import is_second_week


def week_command_handler(message: Message, bot: TeleBot, repository: Repository):
    date = datetime.datetime.fromtimestamp(message.date)

    if is_second_week(date):
        week_text = "верхняя"
    else:
        week_text = "нижняя"

    text = f"Сейчас идёт {week_text} неделя"
    return bot.reply_to(message, text)
