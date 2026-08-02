import asyncio

from app.loader import bot, dp
from app.handlers.user.start import router

async def main():
    dp.include_router(router)

    print("BotForge Catalog запущен!") 
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())