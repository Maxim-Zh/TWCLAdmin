from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from src.filters import IsPrivate
from src.loader import dp


@dp.message_handler(CommandHelp(), IsPrivate())
async def command_help(message: types.Message):
    template = [
        'Список команд:',
        '/start - Начать общение',
        '/help - Получить помощь',
    ]
    text ='\n'.join(template)
    await message.answer(text=text)
