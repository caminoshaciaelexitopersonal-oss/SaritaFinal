from rest_framework import serializers
from apps.admin_plataforma.gestion_operativa.modulos_genericos.costos.models import Costo

class AdminCostoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costo
        fields = '__all__'
        read_only_fields = ['perfil']
