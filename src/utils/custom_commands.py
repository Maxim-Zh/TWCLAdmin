from aiogram import types

async def set_default_commands(dp) -> None:
    await dp.bot.set_my_commands([
        types.BotCommand(command='start',
                         description='Начать общение'),
        types.BotCommand(command='help',
                         description='Получить помощь'),
        types.BotCommand(command='show_commadns',
                         description='Показать клавиатуру с доступными '
                                     'действиями'),
    ])