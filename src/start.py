async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dispatcher=dp, on_startup=on_startup)
   