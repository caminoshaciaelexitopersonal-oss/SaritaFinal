from rest_framework import serializers
from .models import Hotel, Habitacion, GuiaTuristico, VehiculoTuristico, PaqueteTuristico, Reserva
from empresa.serializers import ClienteSerializer # Importar para anidar

class ReservaSerializer(serializers.ModelSerializer):
    cliente_info = ClienteSerializer(source='cliente', read_only=True)

    class Meta:
        model = Reserva
        fields = [
            'id', 'cliente', 'cliente_info', 'fecha_reserva', 'numero_personas',
            'estado', 'notas_reserva', 'fecha_creacion'
        ]
        read_only_fields = ['id', 'fecha_creacion', 'prestador', 'cliente_info']


class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = '__all__'
        read_only_fields = ['hotel']

class HotelSerializer(serializers.ModelSerializer):
    habitaciones = HabitacionSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ['prestador', 'categoria_estrellas', 'reporte_ocupacion_nacional', 'reporte_ocupacion_internacional', 'habitaciones']
        read_only_fields = ['prestador']

class GuiaTuristicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuiaTuristico
        fields = '__all__'
        read_only_fields = ['prestador']

class VehiculoTuristicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiculoTuristico
        fields = '__all__'
        read_only_fields = ['prestador']

class PaqueteTuristicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaqueteTuristico
        fields = '__all__'
        read_only_fields = ['prestador_agencia']