from rest_framework import serializers
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.costos.models import Costo

class CostoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costo
        fields = '__all__'
        read_only_fields = ['perfil']
