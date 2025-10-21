from rest_framework import serializers
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.reportes_estadisticas import Reporte

class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = [
            'id', 'nombre_reporte', 'tipo_reporte', 'fecha_inicio', 'fecha_fin',
            'datos', 'fecha_generacion'
        ]
        read_only_fields = ['datos', 'fecha_generacion']
