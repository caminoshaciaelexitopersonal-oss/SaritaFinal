from rest_framework import serializers
from apps.admin_plataforma.gestion_operativa.modulos_genericos.reservas.models import Reserva, PoliticaCancelacion, ReservaServicioAdicional

class AdminReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
        read_only_fields = ['provider']

class AdminPoliticaCancelacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliticaCancelacion
        fields = '__all__'
        read_only_fields = ['provider']
