from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🎥 Портфолио",
                callback_data="portfolio"
            ),
            InlineKeyboardButton(
                text="💰 Услуги",
                callback_data="services"
            ),
        ],
        [
            InlineKeyboardButton(
                text="👤 Обо мне",
                callback_data="about"
            ),
            InlineKeyboardButton(
                text="📞 Контакты",
                callback_data="contacts"
            ),
        ],
    ]
)