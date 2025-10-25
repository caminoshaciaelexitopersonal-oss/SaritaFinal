from rest_framework import serializers
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.costos import Costo

class CostoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costo
        fields = ['id', 'concepto', 'monto', 'fecha', 'es_recurrente', 'tipo_costo']
