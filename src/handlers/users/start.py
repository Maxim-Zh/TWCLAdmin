from aiogram import types
from random import choice

from filters import IsPrivate
from loader import dp


@dp.message_handler(IsPrivate(), commands=['start'])
async def command_start(message: types.Message):
    username = message.from_user.first_name
    with open(file='src/static/bot_names.txt', encoding='UTF-8') as file:
        lines = file.readlines()
    names = [name.replace('\n', '') for name in lines]
    template = [
        f'Здравствуйте {username}, меня зовут {choice(names)}.',
        'Я ваш персональный помощник по администрированию встроенного '
        'torrent-клиента Keenetic.',
        'Наберите команду /show_commands для отображения клавиатуры с '
        'возможными действиями.',
        'Для отображение всех возможных команд, наберите /help.',
    ]
    text = '\n'.join(template)
    await message.answer(text=text)
