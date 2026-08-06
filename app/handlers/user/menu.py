from aiogram import Router, F
from aiogram.types import CallbackQuery

from data.profile import PROFILE
from app.keyboards.inline_menu import main_menu
from app.keyboards.sections import back_menu

router = Router()


@router.callback_query(F.data == "about")
async def about_callback(callback: CallbackQuery):
    text = (
        f"👤 <b>{PROFILE['name']}</b>\n"
        f"{PROFILE['profession']}\n"
        f"📍 {PROFILE['city']}\n\n"
        f"{PROFILE['about']}"
    )

    await callback.message.edit_text(
        text,
        reply_markup=back_menu
    )

    await callback.answer()


@router.callback_query(F.data == "services")
async def services_callback(callback: CallbackQuery):
    services = "\n".join(PROFILE["services"])

    await callback.message.edit_text(
        f"<b>💰 Мои услуги</b>\n\n{services}",
        reply_markup=back_menu
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

    await callback.message.edit_text(
        text,
        reply_markup=back_menu
    )

    await callback.answer()


@router.callback_query(F.data == "portfolio")
async def portfolio_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        "🎥 <b>Портфолио</b>\n\n"
        "Здесь позже будут фотографии, видео или ссылки на работы.",
        reply_markup=back_menu
    )

    await callback.answer()


@router.callback_query(F.data == "back")
async def back_callback(callback: CallbackQuery):
    text = (
        f"👋 Привет!\n\n"
        f"Меня зовут <b>{PROFILE['name']}</b>.\n"
        f"Я — {PROFILE['profession']}.\n"
        f"📍 {PROFILE['city']}\n\n"
        f"{PROFILE['about']}"
    )

    await callback.message.edit_text(
        text,
        reply_markup=main_menu
    )

    await callback.answer()