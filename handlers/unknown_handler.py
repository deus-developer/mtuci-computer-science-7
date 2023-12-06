from telebot import TeleBot
from telebot.types import Message

from repository import Repository


def unknown_handler(message: Message, bot: TeleBot, repository: Repository):
    return bot.reply_to(message, "Извините, я Вас не понял")
