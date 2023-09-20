from functools import lru_cache

from aiogram import Router, F
from aiogram.types import (
    InlineQuery, InlineQueryResultArticle, InputTextMessageContent,
    InlineQueryResultsButton, WebAppInfo
)

router = Router(name="inline-mode")

data = {
    "Знакомство с aiogram": {"deeplink": "quickstart", "path": "quickstart/"},
    "Работа с сообщениями": {"deeplink": "messages", "path": "messages//"},
    "Экранирование": {"deeplink": "escaping", "path": "messages/#input-escaping"},
    "Сохранение форматирования": {"deeplink": "keep-formatting", "path": "messages/#keep-formatting"},
    "Работа с entities": {"deeplink": "entities", "path": "messages/#message-entities"},
    "Отправка файлов": {"deeplink": "upload", "path": "messages/#uploading-media"},
    "Upload": {"deeplink": "upload", "path": "messages/#uploading-media"},
    "Скачивание файлов": {"deeplink": "download", "path": "messages/#downloading-media"},
    "Download": {"deeplink": "download", "path": "messages/#downloading-media"},
    "Скрытая ссылка": {"deeplink": "hide-image", "path": "messages/#bonus"},
    "Как спрятать ссылку в тексте": {"deeplink": "hide-image", "path": "messages/#bonus"},
    "Кнопки": {"deeplink": "buttons", "path": "buttons/"},
    "Фабрика колбэков": {"deeplink": "callback-factory", "path": "buttons/#callback-factory"},
    "Роутеры": {"deeplink": "routers", "path": "routers/"},
    "Фильтры": {"deeplink": "filters", "path": "filters-and-middlewares/#filters"},
    "Магические фильтры": {"deeplink": "magic", "path": "filters-and-middlewares/#magic-filters"},
    "Магия": {"deeplink": "magic", "path": "filters-and-middlewares/#magic-filters"},
    "Magic Filter": {"deeplink": "magic", "path": "filters-and-middlewares/#magic-filters"},
    "Мидлвари": {"deeplink": "middlewares", "path": "filters-and-middlewares/#middlewares"},
    "My Chat Member": {"deeplink": "my-chat-member", "path": "special-updates/#my-chat-member"},
    "Chat Member": {"deeplink": "chat-member", "path": "special-updates/#chat-member"},
    "FSM": {"deeplink": "fsm", "path": "fsm/"},
    "Конечные автоматы": {"deeplink": "fsm", "path": "fsm/"},
    "Состояния": {"deeplink": "fsm", "path": "fsm/"},
    "Инлайн-режим": {"deeplink": "inline-mode", "path": "inline-mode/"}
}


def make_url(path: str | None) -> str:
    base_url = "https://t.me/aio3bot/guide"
    if path is None:
        return base_url
    return f"{base_url}?startapp={path}"


@lru_cache()
def make_text(title: str, path: str | None) -> str:
    return f"<b>{title}</b>\n{make_url(path)}"


@lru_cache()
def make_link(title: str, deeplink: str) -> InlineQueryResultArticle:
    return InlineQueryResultArticle(
        id=deeplink,
        title=title,
        input_message_content=InputTextMessageContent(
            message_text=make_text(title, deeplink),
            parse_mode="HTML"
        )
    )


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
        results.append(make_link(title, deeplink))
    await inline_query.answer(
        results=results,
        cache_time=10,
        button=InlineQueryResultsButton(
            text="Открыть книгу",
            web_app=WebAppInfo(url="https://mastergroosha.github.io/aiogram-3-guide/")
        )
    )
