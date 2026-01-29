from rest_framework import serializers
from apps.admin_plataforma.gestion_operativa.modulos_genericos.horarios.models import Horario, ExcepcionHorario

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'
        read_only_fields = ['perfil']

class ExcepcionHorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcepcionHorario
        fields = '__all__'
        read_only_fields = ['perfil']
