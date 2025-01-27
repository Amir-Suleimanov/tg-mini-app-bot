import os
from django.core.asgi import get_asgi_application
from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
from aiohttp import web

from dotenv import load_dotenv
import os

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Инициализация Django ASGI приложения
django_application = get_asgi_application()

# Инициализация бота и диспетчера
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

async def on_startup(app):
    await bot.set_webhook(
        "https://127.0.0.1:5173/webhook",
        drop_pending_updates=True
    )

async def on_shutdown(app):
    await bot.delete_webhook()

# Создаем aiohttp приложение для обработки вебхуков
aiohttp_app = web.Application()
aiohttp_app.on_startup.append(on_startup)
aiohttp_app.on_shutdown.append(on_shutdown)

# Регистрируем обработчик вебхуков от Telegram
handler = SimpleRequestHandler(dispatcher=dp, bot=bot)
handler.register(aiohttp_app, path="/webhook")

# Комбинируем Django и aiogram обработчики
async def application(scope, receive, send):
    if scope["type"] == "http" and scope["path"].startswith("/webhook"):
        await aiohttp_app.handle_request(scope, receive, send)
    else:
        await django_application(scope, receive, send)
