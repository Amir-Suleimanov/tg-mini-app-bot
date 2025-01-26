from django.contrib import admin

from .models import Surah, Ayah

# Register your models here.
@admin.register(Surah)
class SurahAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'name', 'ayats_count')

@admin.register(Ayah)
class AyahAdmin(admin.ModelAdmin):
    list_display = ('id', 'surah', 'number', 'text_arabic', 'translation')
