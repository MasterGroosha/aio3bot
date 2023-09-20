from aiogram import Router

from bot.handlers import commands, inline_mode


def get_routers() -> list[Router]:
    return [
        commands.router,
        inline_mode.router
    ]
