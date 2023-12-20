from functools import partial

from telebot import TeleBot
from telebot.custom_filters import TextMatchFilter

from config import settings
from handlers import (
    start_command_handler,
    day_schedule_handler,
    week_schedule_handler,
    mtuci_command_handler,
    help_command_handler,
    unknown_handler,
    week_command_handler,
)
from markups import start_keyboard
from middlewares import DatabaseMiddleware


def main():
    bot = TeleBot(
        token=settings.telegram_bot_token,
        parse_mode="HTML",
        threaded=True,
        num_threads=4,
        use_class_middlewares=True,
        disable_web_page_preview=True,
    )

    bot.setup_middleware(DatabaseMiddleware(database_url=str(settings.database_url)))

    bot.add_custom_filter(TextMatchFilter())

    bot.register_message_handler(
        start_command_handler, pass_bot=True, commands=["start"]
    )

    for weekday, button in enumerate(
        [
            start_keyboard.MONDAY_SCHEDULE_BUTTON_TEXT,
            start_keyboard.TUESDAY_SCHEDULE_BUTTON_TEXT,
            start_keyboard.WEDNESDAY_SCHEDULE_BUTTON_TEXT,
            start_keyboard.THURSDAY_SCHEDULE_BUTTON_TEXT,
            start_keyboard.FRIDAY_SCHEDULE_BUTTON_TEXT,
            start_keyboard.SATURDAY_SCHEDULE_BUTTON_TEXT,
        ],
        1,
    ):
        bot.register_message_handler(
            partial(day_schedule_handler, weekday=weekday), pass_bot=True, text=button
        )

    bot.register_message_handler(
        partial(week_schedule_handler, is_current_week=True),
        pass_bot=True,
        text=[start_keyboard.CURRENT_WEEK_SCHEDULE_BUTTON_TEXT],
    )
    bot.register_message_handler(
        partial(week_schedule_handler, is_current_week=False),
        pass_bot=True,
        text=[start_keyboard.NEXT_WEEK_SCHEDULE_BUTTON_TEXT],
    )
    bot.register_message_handler(week_command_handler, pass_bot=True, commands=["week"])
    bot.register_message_handler(
        mtuci_command_handler, pass_bot=True, commands=["mtuci"]
    )
    bot.register_message_handler(help_command_handler, pass_bot=True, commands=["help"])

    bot.register_message_handler(unknown_handler, pass_bot=True)

    me = bot.get_me()
    print(
        f'Bot ID: {me.id}\n'
        f'Bot Name: {me.first_name}\n'
        f'Bot Username: {me.username}'
    )

    bot.infinity_polling(allowed_updates=["message"])


if __name__ == "__main__":
    main()
