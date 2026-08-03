from aiogram import Router, F
from aiogram.types import Message

from data.profile import PROFILE

router = Router()

@router.message(F.text == "👤 Обо мне")
async def about_handler(message: Message):
    text = (
        f"👤 <b>{PROFILE['name']}</b>\n"
        f"{PROFILE['profession']}\n"
        f"📍 {PROFILE['city']}\n\n"
        f"{PROFILE['about']}"
    )

    await message.answer(text)

@router.message(F.text == "💰 Услуги")
async def services_handler(message: Message):
    services = "\n".join(PROFILE["services"])

    await message.answer(
        f"<b>💰 Мои услуги</b>\n\n{services}"
    )

@router.message(F.text == "📞 Контакты")
async def contacts_handler(message: Message):
    contacts = PROFILE["contacts"]

    text = (
        "<b>📞 Контакты</b>\n\n"
        f"Telegram: {contacts['telegram']}\n"
        f"Телефон: {contacts['phone']}"
    )

    await message.answer(text)

@router.message(F.text == "🎥 Портфолио")
async def portfolio_handler(message: Message):
    await message.answer(
        "🎥 Здесь позже будет портфолио."
    )