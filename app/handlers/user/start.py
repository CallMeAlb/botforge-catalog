from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.keyboards.inline_menu import main_menu
from data.profile import PROFILE

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    text = (
        f"👋 Привет!\n\n"
        f"Меня зовут <b>{PROFILE['name']}</b>.\n"
        f"Я — {PROFILE['profession']}.\n"
        f"📍 {PROFILE['city']}\n\n"
        f"{PROFILE['intro']}"
    )

    await message.answer(
        text,
        reply_markup=main_menu,
    )
