from rest_framework import serializers
from apps.admin_plataforma.gestion_operativa.modulos_genericos.horarios.models import Horario, ExcepcionHorario

class AdminHorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'
        read_only_fields = ['perfil']

class AdminExcepcionHorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcepcionHorario
        fields = '__all__'
        read_only_fields = ['perfil']
