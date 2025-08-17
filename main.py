import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from app.config import BOT_TOKEN
from app.bot.routers import main_menu, guide, subscription, profile, support, partners

async def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN is missing in .env")
    bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    # register routers
    dp.include_router(main_menu.router)
    dp.include_router(guide.router)
    dp.include_router(subscription.router)
    dp.include_router(profile.router)
    dp.include_router(support.router)
    dp.include_router(partners.router)
    print("Bot is running…")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
