from aiogram import Router, F
from aiogram.types import CallbackQuery

from data.profile import PROFILE

router = Router()


@router.callback_query(F.data == "about")
async def about_callback(callback: CallbackQuery):
    text = (
        f"👤 <b>{PROFILE['name']}</b>\n"
        f"{PROFILE['profession']}\n"
        f"📍 {PROFILE['city']}\n\n"
        f"{PROFILE['about']}"
    )

    await callback.message.answer(text)
    await callback.answer()


@router.callback_query(F.data == "services")
async def services_callback(callback: CallbackQuery):
    services = "\n".join(PROFILE["services"])

    await callback.message.answer(
        f"<b>💰 Мои услуги</b>\n\n{services}"
    )

    await callback.answer()


@router.callback_query(F.data == "contacts")
async def contacts_callback(callback: CallbackQuery):
    contacts = PROFILE["contacts"]

    text = (
        "<b>📞 Контакты</b>\n\n"
        f"Telegram: {contacts['telegram']}\n"
        f"Телефон: {contacts['phone']}"
    )

    await callback.message.answer(text)
    await callback.answer()


@router.callback_query(F.data == "portfolio")
async def portfolio_callback(callback: CallbackQuery):
    await callback.message.answer(
        "🎥 Здесь позже будет портфолио."
    )

    await callback.answer()