async def on_startup(dp):
    import filters
    import middlewares
    from utils import set_default_commands
    filters.setup(dp=dp)
    await set_default_commands(dp=dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dispatcher=dp, on_startup=on_startup)
