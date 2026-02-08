from rest_framework import serializers
from apps.admin_plataforma.gestion_operativa.modulos_especializados.guias.models import Skill, TourDetail

class AdminSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'nombre']

class AdminTourDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourDetail
        fields = ['id', 'nombre_guia']
