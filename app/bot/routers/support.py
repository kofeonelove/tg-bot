from aiogram import Router, F
from aiogram.types import Message
from app.config import SUPPORT_USERNAME

router = Router(name="support")

@router.message(F.text == "Help")
async def help_cmd(m: Message):
    await m.answer(f"If you need assistance, contact support: {SUPPORT_USERNAME}")
