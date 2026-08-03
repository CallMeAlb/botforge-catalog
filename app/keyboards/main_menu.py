from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎥 Портфолио"),
            KeyboardButton(text="💰 Услуги"),
        ],
        [
            KeyboardButton(text="👤 Обо мне"),
            KeyboardButton(text="📞 Контакты"),
        ],
    ],
    resize_keyboard=True,
)