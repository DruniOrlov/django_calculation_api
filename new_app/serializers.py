from rest_framework import serializers

from .models import Calculations


class CalculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculations
        fields = '__all__'


class RawDataSerializer(serializers.Serializer):
    date_start = serializers.DateField()
    date_fin = serializers.DateField()
    lag = serializers.IntegerField
