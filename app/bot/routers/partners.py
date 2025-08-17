from aiogram import Router, F
from aiogram.types import Message

router = Router(name="partners")

@router.message(F.text == "Partners")
async def partners(m: Message):
    await m.answer("Partner program coming soon. Invite users and earn bonus days.")
