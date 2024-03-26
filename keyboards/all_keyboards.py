from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def start_kb():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Наш сайт", url="https://mypizza.kg")
            ],
            [
                InlineKeyboardButton(text="Наш инстаграм", url="https://mypizza.kg"),
                InlineKeyboardButton(text="Наш твиттер", url="https://mypizza.kg")
            ],
            [
                InlineKeyboardButton(text="О нас", callback_data="about")
            ],
            [
                InlineKeyboardButton(text="Наше меню", callback_data="our_menu")
            ],
            [
                InlineKeyboardButton(text="Показать объявления", callback_data="parse_cars")
            ]
        ]
    )
    return kb