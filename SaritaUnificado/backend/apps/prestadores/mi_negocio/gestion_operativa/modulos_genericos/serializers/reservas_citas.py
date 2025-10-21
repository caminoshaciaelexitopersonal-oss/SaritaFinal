from rest_framework import serializers
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.reservas_citas import Reserva

class ReservaSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente.nombre', read_only=True)
    producto_nombre = serializers.CharField(source='producto_servicio.nombre', read_only=True)

    class Meta:
        model = Reserva
        fields = [
            'id', 'cliente', 'cliente_nombre', 'producto_servicio', 'producto_nombre',
            'fecha_hora_inicio', 'fecha_hora_fin', 'estado', 'notas', 'monto_total'
        ]
        read_only_fields = ['cliente_nombre', 'producto_nombre']
