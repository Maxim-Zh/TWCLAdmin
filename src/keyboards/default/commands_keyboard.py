from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config.button_text import CMD_1, CMD_2, CMD_3

CMD_KEYBOARD = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text=CMD_1)],
        [KeyboardButton(text=CMD_2), KeyboardButton(CMD_3)],
    ], resize_keyboard=True
)
