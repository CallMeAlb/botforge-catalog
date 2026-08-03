import asyncio

from app.loader import bot, dp

from app.handlers.user.start import router as start_router
from app.handlers.user.menu import router as menu_router

async def main():
    dp.include_router(start_router)
    dp.include_router(menu_router)

    print("BotForge Catalog запущен!") 
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())