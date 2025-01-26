# quran_backend/urls.py
from django.contrib import admin
from django.urls import path, include
# from .asgi import handle_telegram_webhook

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('surahs.urls')),
]