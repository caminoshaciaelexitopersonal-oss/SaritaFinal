from rest_framework import serializers
from apps.admin_plataforma.gestion_operativa.modulos_genericos.valoraciones.models import Valoracion

class AdminValoracionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valoracion
        fields = '__all__'

class AdminRespuestaPrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valoracion
        fields = ['id', 'comentario']
