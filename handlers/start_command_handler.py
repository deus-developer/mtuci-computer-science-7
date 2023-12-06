from telebot import TeleBot
from telebot.types import Message

from markups import START_KEYBOARD_REPLY_MARKUP
from repository import Repository


def start_command_handler(message: Message, bot: TeleBot, repository: Repository):
    return bot.reply_to(message, text="...", reply_markup=START_KEYBOARD_REPLY_MARKUP)
