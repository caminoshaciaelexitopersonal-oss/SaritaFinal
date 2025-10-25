from rest_framework import serializers
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.soporte_ayuda import TicketSoporte

class TicketSoporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketSoporte
        fields = ['id', 'asunto', 'mensaje', 'estado', 'fecha_creacion', 'fecha_actualizacion']
        read_only_fields = ['estado', 'fecha_creacion', 'fecha_actualizacion']
