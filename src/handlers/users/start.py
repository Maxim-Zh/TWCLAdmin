from aiogram import types

from src.filters import IsPrivate
from src.loader import dp


@dp.message_handler(IsPrivate(), commands=['start'])
async def command_start(message: types.Message):
    await message.answer(text='answer to call')
