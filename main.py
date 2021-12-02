import asyncio
from pytgcalls import idle
from driver.Annie import call_py, bot

async def mulai_bot():
    print("[ANNIE]: STARTING BOT CLIENT")
    await bot.start()
    print("[ANNIE]: STARTING PYTGCALLS CLIENT")
    await call_py.start()
    await idle()
    await pidle()
    print("[ANNIE]: STOPPING BOT & USERBOT")
    await bot.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(mulai_bot())
