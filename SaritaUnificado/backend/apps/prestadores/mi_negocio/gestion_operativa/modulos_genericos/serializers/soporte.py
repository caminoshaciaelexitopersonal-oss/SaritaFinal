# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/serializers/soporte.py
from rest_framework import serializers
from apps.prestadores.models import TicketSoporte

class TicketSoporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketSoporte
        fields = '__all__'
