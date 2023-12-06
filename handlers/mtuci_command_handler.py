from telebot import TeleBot
from telebot.types import Message

from repository import Repository


def mtuci_command_handler(message: Message, bot: TeleBot, repository: Repository):
    return bot.reply_to(message, "МТУСИ – https://mtuci.ru/")
