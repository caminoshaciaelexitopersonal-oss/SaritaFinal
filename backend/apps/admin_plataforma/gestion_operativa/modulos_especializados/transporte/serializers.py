from rest_framework import serializers
from apps.prestadores.mi_negocio.gestion_operativa.modulos_especializados.transporte.models import Vehicle #, MaintenanceOrder

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [
            'id', 'nombre', 'placa', 'modelo_ano', 'tipo_vehiculo',
            'capacidad', 'status', 'insurance_expiry_date', 'tech_inspection_expiry_date'
        ]

# class MaintenanceOrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MaintenanceOrder
#         fields = '__all__'
