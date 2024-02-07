

import asyncio
import importlib
import os

from pyrogram import idle

from ShahmMusic import (
    ASS_ID,
    ASS_NAME,
    ASS_USERNAME,
    BOT_ID,
    BOT_NAME,
    BOT_USERNAME,
    LOGGER,
    SUNAME,
    app,
    app2,
    pytgcalls,
)
from ShahmMusic.Modules import ALL_MODULES


async def fallen_startup():
    LOGGER.info("[•] Loading Modules...")
    for module in ALL_MODULES:
        importlib.import_module("ShahmMusic.Modules." + module)
    LOGGER.info(f"[•] Loaded {len(ALL_MODULES)} Modules.")

    LOGGER.info("[•] Refreshing Directories...")
    if "downloads" not in os.listdir():
        os.mkdir("downloads")
    if "cache" not in os.listdir():
        os.mkdir("cache")
    LOGGER.info("[•] Directories Refreshed.")

    try:
        await app.send_message(
            SUNAME,
            f"✯ بــــوت 🦈 شارك الجديد ✯\n\n⌔︙ الايدي: `{BOT_ID}`\n⌔︙ الاسم : {BOT_NAME}\n⌔︙ الاسم : @{BOT_USERNAME}",
        )
    except:
        LOGGER.error(
            f"{BOT_NAME} failed to send message at @{SUNAME}, please go & check."
        )

    try:
        await app2.send_message(
            SUNAME,
            f"✯ بــــوت🦈 شارك الجديد ✯\n\n⌔︙ الايدي: `{ASS_ID}`\n⌔︙ الاسم : {ASS_NAME}\n⌔︙ الاسم : @{ASS_USERNAME}",
        )
    except:
        LOGGER.error(
            f"{ASS_NAME} فشل ارسال رساله @{SUNAME}, يرجى التحقق ."
        )

    await app2.send_message(BOT_USERNAME, "/start")

    LOGGER.info(f"[•] بدأ تشغيل {BOT_NAME}.")
    LOGGER.info(f"[•] Assistant Started As {ASS_NAME}.")

    LOGGER.info(
        "[•] \x53\x74\x61\x72\x74\x69\x6e\x67\x20\x50\x79\x54\x67\x43\x61\x6c\x6c\x73\x20\x43\x6c\x69\x65\x6e\x74\x2e\x2e\x2e"
    )
    await pytgcalls.start()
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(fallen_startup())
    LOGGER.error("Shahm Music Bot Stopped.")
