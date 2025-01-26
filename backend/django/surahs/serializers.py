# surahs/serializers.py
from rest_framework import serializers
from .models import Surah

class SurahSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surah
        fields = ['number', 'name', 'ayats_count']