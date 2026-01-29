from rest_framework import serializers
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.valoraciones.models import Valoracion

class ValoracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valoracion
        fields = '__all__'

class RespuestaPrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valoracion
        fields = ['respuesta_prestador']
