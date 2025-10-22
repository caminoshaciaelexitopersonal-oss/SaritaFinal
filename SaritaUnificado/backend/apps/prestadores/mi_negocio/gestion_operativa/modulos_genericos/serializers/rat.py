# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/serializers/rat.py
from rest_framework import serializers
from apps.prestadores.models import RegistroActividadTuristica

class RegistroActividadTuristicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroActividadTuristica
        fields = '__all__'

 