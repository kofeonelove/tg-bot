from aiogram import Router, F
from aiogram.types import Message
from app.keyboards import main_menu

router = Router(name="main_menu")

@router.message(F.text.in_({"/start", "start"}))
async def start(m: Message):
    await m.answer(
        "Welcome! Unlock privacy and security with our VPN.\n\nChoose an option:",
        reply_markup=main_menu
    )
