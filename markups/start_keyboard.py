from telebot.types import ReplyKeyboardMarkup

MONDAY_SCHEDULE_BUTTON_TEXT = "Понедельник"
TUESDAY_SCHEDULE_BUTTON_TEXT = "Вторник"
WEDNESDAY_SCHEDULE_BUTTON_TEXT = "Среда"
THURSDAY_SCHEDULE_BUTTON_TEXT = "Четверг"
FRIDAY_SCHEDULE_BUTTON_TEXT = "Пятница"
SATURDAY_SCHEDULE_BUTTON_TEXT = "Суббота"

CURRENT_WEEK_SCHEDULE_BUTTON_TEXT = "Расписание на текущую неделю"
NEXT_WEEK_SCHEDULE_BUTTON_TEXT = "Расписание на следующую неделю"


START_KEYBOARD_REPLY_MARKUP = ReplyKeyboardMarkup(
    resize_keyboard=True,
    is_persistent=True,
)
START_KEYBOARD_REPLY_MARKUP.add(
    MONDAY_SCHEDULE_BUTTON_TEXT,
    TUESDAY_SCHEDULE_BUTTON_TEXT,
    WEDNESDAY_SCHEDULE_BUTTON_TEXT,
    THURSDAY_SCHEDULE_BUTTON_TEXT,
    FRIDAY_SCHEDULE_BUTTON_TEXT,
    SATURDAY_SCHEDULE_BUTTON_TEXT,
)
START_KEYBOARD_REPLY_MARKUP.row(CURRENT_WEEK_SCHEDULE_BUTTON_TEXT)
START_KEYBOARD_REPLY_MARKUP.row(NEXT_WEEK_SCHEDULE_BUTTON_TEXT)
