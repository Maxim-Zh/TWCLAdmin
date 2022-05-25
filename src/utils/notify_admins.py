from aiogram import Dispatcher

from config.settings import ADMINS_ID

async def on_startup_notify(dp: Dispatcher):
    for id in ADMINS_ID:
        await dp.bot.send_message(chat_id=id,
                                  text='Бот запущен и готов к работе')