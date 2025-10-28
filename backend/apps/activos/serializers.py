# backend/apps/activos/serializers.py
from rest_framework import serializers
from .models import ActivoFijo, RegistroDepreciacion

class ActivoFijoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivoFijo
        fields = '__all__'
        read_only_fields = ['perfil', 'depreciacion_acumulada', 'valor_en_libros']

class RegistroDepreciacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroDepreciacion
        fields = '__all__'
