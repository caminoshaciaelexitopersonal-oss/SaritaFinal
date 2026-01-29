from rest_framework import serializers
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.reservas.models import Reserva, PoliticaCancelacion, ReservaServicioAdicional

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
        read_only_fields = ['provider']

class PoliticaCancelacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliticaCancelacion
        fields = '__all__'
        read_only_fields = ['provider']
