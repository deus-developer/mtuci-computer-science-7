from telebot import TeleBot
from telebot.types import Message

from repository import Repository

HELP_DOCUMENTATION_TEXT = """
<b>Документация</b>

Расписание по дням недели:
- Понедельник
- Вторник
- Среда
- Четверг
- Пятница
- Суббота

/week - Информация о текущей недели (Верхняя или нижняя)
/mtuci - Ссылка на официальный сайт МТУСИ

"""


def help_command_handler(message: Message, bot: TeleBot, repository: Repository):
    return bot.reply_to(message, HELP_DOCUMENTATION_TEXT)
