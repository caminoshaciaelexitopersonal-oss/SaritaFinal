# backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_especializados/serializers/transporte.py
from rest_framework import serializers
from apps.prestadores.models import Vehiculo, Conductor

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = [
            'id', 'placa', 'marca', 'modelo', 'año',
            'capacidad_pasajeros', 'tipo_vehiculo', 'foto',
            'soat_vigente', 'tecnomecanica_vigente', 'perfil'
        ]
        read_only_fields = ['id']

class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = [
            'id', 'nombre', 'apellido', 'cedula', 'telefono', 'foto',
            'licencia_conduccion', 'vencimiento_licencia', 'user', 'perfil'
        ]
        read_only_fields = ['id']
