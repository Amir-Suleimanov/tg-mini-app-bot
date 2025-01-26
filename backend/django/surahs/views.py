# quran_reader/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Surah, Ayah
from rest_framework.decorators import api_view
import logging
from rest_framework import status

logger = logging.getLogger(__name__)


class SurahListView(APIView):
    def get(self, request):
        surahs = Surah.objects.all().values('number', 'name', 'ayats_count')
        return Response(surahs)


@api_view(['GET'])
def surah_detail(request, surah_number):
    logger.info(f"Запрос к суре #{surah_number}")
    try:
        surah = Surah.objects.get(number=surah_number)
        ayahs = surah.ayahs.all().values('number', 'text_arabic', 'translation')
        data = {
            'number': surah.number,
            'name': surah.name,
            'ayahs': list(ayahs)
        }
        return Response(data)
    except Surah.DoesNotExist:
        logger.error(f"Сура #{surah_number} не найдена")
        return Response(
            {'error': f'Surah {surah_number} not found'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        logger.critical(f"Ошибка: {str(e)}", exc_info=True)
        return Response(
            {'error': 'Internal server error'}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


