import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router

from bot.handlers import get_routers

router = Router()


async def main() -> None:
    bot = Bot('')
    dp = Dispatcher()
    dp.include_routers(*get_routers())
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
