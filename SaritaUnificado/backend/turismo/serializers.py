from rest_framework import serializers
from .models import Hotel, Habitacion, ReservaTuristica, GuiaTuristico, VehiculoTuristico, PaqueteTuristico

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

class ReservaTuristicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaTuristica
        fields = '__all__'
        read_only_fields = ('prestador', 'usuario')

class GuiaTuristicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuiaTuristico
        fields = '__all__'
        read_only_fields = ('prestador',)

class VehiculoTuristicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiculoTuristico
        fields = '__all__'
        read_only_fields = ('prestador',)

class PaqueteTuristicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaqueteTuristico
        fields = '__all__'
        read_only_fields = ('prestador',)