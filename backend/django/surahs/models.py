# quran_reader/models.py
from django.db import models

class Surah(models.Model):
    number = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    ayats_count = models.IntegerField()

    def __str__(self):
        return self.name


class Ayah(models.Model):
    surah = models.ForeignKey(Surah, related_name='ayahs', on_delete=models.CASCADE)
    number = models.IntegerField()
    text_arabic = models.TextField()
    translation = models.TextField()

    def __str__(self):
        return f"{self.surah.number}:{self.number}"