from aiogram import types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove

from keyboards import CMD_KEYBOARD
from loader import dp
from config.button_text import CMD_1, CMD_2, CMD_3


@dp.message_handler(commands=['show_commands'])
async def show_commands(message: types.Message):
    await message.answer('Выберите действие из клавиатуры ниже',
                         reply_markup=CMD_KEYBOARD)


@dp.message_handler(Text(equals=CMD_1))
async def answer_to_CMD_1(message: types.Message):
    await message.reply(f'Выбрана {message.text}',
                        reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Text(equals=CMD_2))
async def answer_to_CMD_1(message: types.Message):
    await message.reply(f'Выбрана {message.text}',
                        reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Text(equals=CMD_3))
async def answer_to_CMD_1(message: types.Message):
    await message.reply(f'Выбрана {message.text}',
                        reply_markup=ReplyKeyboardRemove())
