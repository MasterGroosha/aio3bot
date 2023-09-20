from functools import lru_cache
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

router = Router(name="commands")


@lru_cache(maxsize=1)
def make_switch_to_inline_kb() -> InlineKeyboardMarkup:
    button = InlineKeyboardButton(
        text="Попробовать инлайн-режим",
        switch_inline_query_current_chat=""
    )
    return InlineKeyboardMarkup(inline_keyboard=[[button]])


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Нажми на кнопку и попробуй ввести текст, например, 'fsm' или 'особые апдейты' (без кавычек) ",
        reply_markup=make_switch_to_inline_kb()
    )
