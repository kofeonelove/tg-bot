from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from app.keyboards import guide_devices_kb

router = Router(name="guide")

@router.message(F.text == "📘 Guide")
async def choose_device(m: Message):
    await m.answer("Select your device:", reply_markup=guide_devices_kb)

@router.callback_query(F.data.startswith("guide:"))
async def send_steps(c: CallbackQuery):
    target = c.data.split(":")[1]
    text = {
        "windows": (
            "Guide for Windows:\n"
            "1) Download and install **V2RayTun**.\n"
            "2) Copy your subscription key to clipboard.\n"
            "3) Open V2RayTun (Run as Administrator if needed).\n"
            "4) Tap the ➕ in the top-right → **Add from clipboard**. The profile will appear.\n"
            "5) Tap the center to connect."
        ),
        "android": (
            "Guide for Android:\n"
            "1) Install **v2rayNG** from Google Play.\n"
            "2) Copy your subscription key.\n"
            "3) Open v2rayNG → **Subscribe from clipboard**.\n"
            "4) Tap the big button to connect."
        ),
        "ios": (
            "Guide for iPhone (iOS):\n"
            "1) Install **Shadowrocket** (or **V2RayN-E**).\n"
            "2) Copy your subscription key.\n"
            "3) Open the app → **Add from clipboard**.\n"
            "4) Allow VPN profile → Connect."
        ),
        "mac": (
            "Guide for Mac:\n"
            "1) Install **V2RayN-Mac** (or **Shadowrocket** for Apple Silicon via iOS).\n"
            "2) Copy your subscription key.\n"
            "3) Open the app → **Add from clipboard**.\n"
            "4) Connect from the status bar."
        ),
    }.get(target, "Device not recognized.")
    await c.message.answer(text, disable_web_page_preview=True)
    await c.answer()
