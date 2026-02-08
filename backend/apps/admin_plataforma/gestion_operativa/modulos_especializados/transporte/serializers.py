from rest_framework import serializers
from apps.admin_plataforma.gestion_operativa.modulos_especializados.transporte.models import Vehicle

class AdminVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'placa', 'modelo']
