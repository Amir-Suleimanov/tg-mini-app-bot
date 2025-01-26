# quran_reader/urls.py
from django.urls import path
from .views import SurahListView, surah_detail

urlpatterns = [
    path('surahs/<int:surah_number>/', surah_detail, name='surah-detail'),
    path('surahs/', SurahListView.as_view(), name='surah-list'),
]