import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config.settings import BOT_TOKEN

logging.basicConfig(format=u'(filename)s [LINE:%(lineno)d] #%(levelname)-8s '
                           u'[%(asctime)s] %(message)s')

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, loop=asyncio.get_event_loop(), storage=storage)
