from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from src.loader import dp


@dp.message_handler(CommandStart())
async def command_start(message: types.Message):
    await message.answer(text='answer to call')
