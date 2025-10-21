from rest_framework import serializers
from apps.prestadores.models import Habitacion, ServicioAdicionalHotel

class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = [
            'id', 'nombre_habitacion', 'tipo_habitacion', 'capacidad',
            'precio_base', 'descripcion', 'disponible'
        ]

class ServicioAdicionalHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicioAdicionalHotel
        fields = ['id', 'nombre_servicio', 'descripcion', 'precio']
