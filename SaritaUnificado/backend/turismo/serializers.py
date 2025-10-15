 from rest_framework import serializers
from .models import Hotel, Habitacion, Reserva


class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = '__all__'
        read_only_fields = ['hotel']


class HotelSerializer(serializers.ModelSerializer):
    habitaciones = HabitacionSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = [
            'prestador',
            'categoria_estrellas',
            'reporte_ocupacion_nacional',
            'reporte_ocupacion_internacional',
            'habitaciones'
        ]
        read_only_fields = ['prestador']


class ReservaSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(
        source='cliente.username',
        read_only=True,
        allow_null=True
    )

    class Meta:
        model = Reserva
        fields = '__all__'
        read_only_fields = ['prestador', 'cliente']