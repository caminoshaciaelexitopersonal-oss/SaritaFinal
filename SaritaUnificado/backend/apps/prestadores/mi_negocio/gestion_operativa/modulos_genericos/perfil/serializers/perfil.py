# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/perfil/serializers/perfil.py
from rest_framework import serializers
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.models import Perfil

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'
