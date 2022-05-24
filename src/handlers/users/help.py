from aiogram import types

from src.filters import IsPrivate
from src.loader import dp


@dp.message_handler(IsPrivate(), commands=['help'])
async def command_help(message: types.Message):
    template = [
        'Список команд:',
        '/start - Начать общение',
        '/help - Получить помощь',
    ]
    text ='\n'.join(template)
    await message.answer(text=text)
