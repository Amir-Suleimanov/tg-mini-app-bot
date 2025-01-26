import asyncio
from aiohttp import web
from aiogram import Bot, Dispatcher, types, Router, F
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
from aiogram.client.session.aiohttp import AiohttpSession
import logging

from dotenv import load_dotenv
import os

load_dotenv()
# Включаем логирование
logging.basicConfig(level=logging.INFO)

class ChatTypeFilter:
    def __init__(self, chat_types: list[str]):
        self.chat_types = chat_types

    async def __call__(self, message: types.Message) -> bool:
        return message.chat.type in self.chat_types



ALLOWED_UPDATES = [
    'message',
    'edited_message',
    'channel_post',
    'edited_channel_post',
    'inline_query',
    'chosen_inline_result',
    'callback_query',
    'shipping_query',
    'pre_checkout_query',
    'poll',
    'poll_answer',
    'my_chat_member',
    'chat_member',
    'chat_join_request'
]


# Инициализация бота с кастомной сессией
session = AiohttpSession()
bot = Bot(token=os.getenv('TOKEN'), session=session)
dp = Dispatcher()

user_pr_router = Router()
user_pr_router.message.filter(ChatTypeFilter(["private"]))

@user_pr_router.message(CommandStart())
@user_pr_router.message(F.text.lower() == "старт")
async def start(message: types.Message):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="Open Mini App", 
                web_app=WebAppInfo(url=os.getenv('WebAppURL'))
            )]
        ]
    )
    await message.answer(
        "Нажмите кнопку, чтобы открыть приложение:",
        reply_markup=markup
    )

# Регистрируем роутер
dp.include_router(user_pr_router)

# Создаем aiohttp приложение
app = web.Application()

# Настройка вебхука
async def on_startup(app):
    await bot.set_webhook(
        url=os.getenv('WEBHOOK_URL'),
        drop_pending_updates=True
    )

async def on_shutdown(app):
    await bot.session.close()
    await dp.storage.close()

# Регистрируем обработчик вебхуков
handler = SimpleRequestHandler(dispatcher=dp, bot=bot)
handler.register(app, path="/webhook")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)
    

# Запуск приложения
if __name__ == "__main__":
    asyncio.run(main())
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    web.run_app(app, port=8001, host='0.0.0.0')