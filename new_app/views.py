from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import QueryDict
import pandas as pd
from kernel import main as calculate

from .models import Calculations
from .serializers import CalculationSerializer, RawDataSerializer


class CalculationListOf10View(APIView):
    '''
    Вьюшка принимает гет запрос, возвращает 10 последних записей из БД

    {
    "id": (id записи),
    "date": (дата проведения вычисления),
    "liquid": (жидкость),
    "oil": (нефть),
    "water": (вода),
    "wct": (обводненность)
    }....

    '''

    def get(self, request):
        calculations = Calculations.objects.order_by('-id')[0:10]
        serializer = CalculationSerializer(calculations, many=True)
        return Response(serializer.data)


class CalculationById(APIView):
    '''
    Вьюшка принимает гет запрос, в строке гет запроса необходимо передать ID необходимого измерения, возвращает ответ в
    виде JSON структуры слудующего вида:

    {
    "id": (id записи),
    "date": (дата проведения вычисления),
    "liquid": (жидкость),
    "oil": (нефть),
    "water": (вода),
    "wct": (обводненность)
    }
    
    '''
    def get(self, request, id):
        calculations = Calculations.objects.get(id=id)
        serializer = CalculationSerializer(calculations)
        return Response(serializer.data)


class CalculationCreate(APIView):
    '''

    Вьюшка принимает пост запрос, передает его в функцию, вывод функции записывает в базу данных
    Принимает пост запрос следующей структуры:

    date_start - дата в формате "ГГГГ-ММ-ДД"
    date-fin - дата в формате "ГГГГ-ММ-ДД"
    lag - целое число

    '''
    def post(self, request):
        raw_data = RawDataSerializer(data=request.data)
        print(request.data)
        if raw_data.is_valid():
            df = calculate(raw_data.data.get('date_start'), raw_data.data.get('date_fin'), raw_data.data.get('lag'))
            final_data = {'date': df.iloc[0]['date'].strftime('%Y-%m-%d'),
                          'liquid': df.iloc[0]['liquid'],
                          'oil': df.iloc[0]['oil'],
                          'water': df.iloc[0]['water'],
                          'wct': df.iloc[0]['wct']}
            query_dict = QueryDict('', mutable=True)
            query_dict.update(final_data)
            calculation = CalculationSerializer(data=query_dict)
            if calculation.is_valid():
                calculation.save()
                return Response(calculation.data)
            else:
                return Response(status=500)