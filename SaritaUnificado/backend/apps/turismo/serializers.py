from rest_framework import serializers
from .models import Hotel, Habitacion, Tarifa, Disponibilidad, Reserva
from api.models import RutaTuristica
# from apps.prestadores.mi_negocio.serializers.clientes import ClienteSerializer

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

class TarifaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarifa
        fields = '__all__'
        read_only_fields = ['prestador']

class DisponibilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disponibilidad
        fields = '__all__'
        read_only_fields = ['prestador']

class ReservaSerializer(serializers.ModelSerializer):
    # cliente_info = ClienteSerializer(source='cliente', read_only=True)
    class Meta:
        model = Reserva
        fields = [
            'id', 'cliente', 'content_type', 'object_id',
            'fecha_inicio_reserva', 'fecha_fin_reserva', 'numero_personas',
            'estado', 'monto_total', 'notas_reserva'
        ]
        read_only_fields = ['id', 'prestador', 'monto_total']

class RutaTuristicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RutaTuristica
        fields = ['id', 'nombre', 'slug', 'descripcion', 'imagen_principal', 'es_publicado']