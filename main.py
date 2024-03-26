import asyncio
import logging
from aiogram import Bot

from bot import bot, dp, db
from handlers.start import start_router
from handlers.picture import picture_router
from handlers.echo import echo_router
from handlers.our_menu import menu_router
from handlers.survey import survey_router
from handlers.mashina_parser import mashina_router


async def on_startup(bot: Bot):
    db.drop_tables()
    db.create_tables()
    db.populate_tables()


async def main():
    # регистрация роутеров
    dp.include_router(start_router)
    dp.include_router(picture_router)
    dp.include_router(menu_router)
    dp.include_router(survey_router)
    dp.include_router(mashina_router)

    # в самом конце
    dp.include_router(echo_router)

    dp.startup.register(on_startup)
    # запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())