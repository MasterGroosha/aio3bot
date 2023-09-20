from functools import lru_cache

from aiogram import Router, F
from aiogram.types import (
    InlineQuery, InlineQueryResultArticle, InputTextMessageContent,
    InlineQueryResultsButton, WebAppInfo
)

router = Router(name="inline-mode")

data = {
    "Знакомство с aiogram": "quickstart",
    "Работа с сообщениями": "messages",
    "Экранирование": "escaping",
    "Работа с entities": "entities",
    "Сохранение форматирования": "keep-formatting",
    "Отправка файлов": "upload",
    "Upload": "upload",
    "Скачивание файлов": "download",
    "Download": "download",
    "Как спрятать ссылку в текста": "hide-image",
    "Скрытая ссылка": "hide-image",
    "Кнопки": "buttons",
    "Фабрика колбэков": "callback-factory",
    "Роутеры": "routers",
    "Фильтры": "filters",
    "Магия": "magic",
    "magic filter": "magic",
    "Мидлвари": "middlewares",
    "My Chat Member": "my-chat-member",
    "Chat Member": "chat-member",
    "FSM": "fsm",
    "Конечные автоматы": "fsm",
    "Состояния": "fsm",
    "Инлайн-режим": "inline-mode",
}


def make_url(path: str) -> str:
    return f"https://t.me/aio3bot/guide?startapp={path}"


@lru_cache()
def make_text(title: str, path: str) -> str:
    return f"<b>{title}</b>\n{make_url(path)}"


@router.inline_query(F.query.len() > 0)
async def filtered_search(inline_query: InlineQuery):
    pass


@router.inline_query()
async def empty_search(inline_query: InlineQuery):
    results = list()
    seen_urls = set()
    for title, deeplink in data.items():
        if deeplink in seen_urls:
            continue
        seen_urls.add(deeplink)
        link = InlineQueryResultArticle(
            id=deeplink,
            title=title,
            input_message_content=InputTextMessageContent(
                message_text=make_text(title, deeplink),
                parse_mode="HTML"
            )
        )
        results.append(link)
    await inline_query.answer(
        results=results,
        cache_time=10,
        button=InlineQueryResultsButton(
            text="Открыть книгу",
            web_app=WebAppInfo(url="https://mastergroosha.github.io/aiogram-3-guide/")
        )
    )
