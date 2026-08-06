from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.profile import PROFILE


back_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="⬅️ Назад",
                callback_data="back"
            )
        ]
    ]
)


def contacts_menu():
    buttons = []

    links = PROFILE["links"]

    if links["telegram"]:
        buttons.append([
            InlineKeyboardButton(
                text="💬 Telegram",
                url=links["telegram"]
            )
        ])

    if links["vk"]:
        buttons.append([
            InlineKeyboardButton(
                text="📘 VK",
                url=links["vk"]
            )
        ])

    if links["website"]:
        buttons.append([
            InlineKeyboardButton(
                text="🌐 Сайт",
                url=links["website"]
            )
        ])

    if links["portfolio"]:
        buttons.append([
            InlineKeyboardButton(
                text="🎥 Портфолио",
                url=links["portfolio"]
            )
        ])

    buttons.append([
        InlineKeyboardButton(
            text="⬅️ Назад",
            callback_data="back"
        )
    ])

    return InlineKeyboardMarkup(
        inline_keyboard=buttons
    )