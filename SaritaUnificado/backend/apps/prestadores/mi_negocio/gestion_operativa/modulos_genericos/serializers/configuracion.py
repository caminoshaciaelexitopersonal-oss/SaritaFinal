# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/serializers/configuracion.py
from rest_framework import serializers
from apps.prestadores.models import ConfiguracionPrestador

class ConfiguracionPrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfiguracionPrestador
        fields = '__all__'
