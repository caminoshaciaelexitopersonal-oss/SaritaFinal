from rest_framework import serializers
from .models import Reserva, PoliticaCancelacion, ReservaServicioAdicional
from ..productos_servicios.serializers import ProductSerializer
from ..clientes.serializers import ClienteSerializer

class PoliticaCancelacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliticaCancelacion
        fields = '__all__'
        read_only_fields = ('perfil',)

class ReservaServicioAdicionalSerializer(serializers.ModelSerializer):
    servicio_id = serializers.UUIDField(source='servicio_ref_id')

    class Meta:
        model = ReservaServicioAdicional
        fields = ('servicio_id', 'cantidad', 'precio_unitario')

class ReservaSerializer(serializers.ModelSerializer):
    servicios_adicionales = ReservaServicioAdicionalSerializer(many=True, required=False)
    # producto_info = ProductSerializer(source='producto', read_only=True)
    cliente_id = serializers.UUIDField(source='cliente_ref_id')
    # cliente_info = ClienteSerializer(source='cliente', read_only=True)

    class Meta:
        model = Reserva
        fields = [
            'id', 'cliente_id', 'estado',
            'fecha_inicio', 'fecha_fin',
            'precio_total', 'deposito_pagado',
            'notas',
            'servicios_adicionales',
            # 'cliente_info'
        ]
        read_only_fields = ('perfil',)

    def create(self, validated_data):
        servicios_data = validated_data.pop('servicios_adicionales', [])
        # TODO: Lógica para calcular costo_total basado en costo_base, impuestos y servicios
        # validated_data['costo_total'] = validated_data.get('costo_base', 0) + validated_data.get('impuestos', 0)
        reserva = Reserva.objects.create(**validated_data)
        for servicio_data in servicios_data:
            ReservaServicioAdicional.objects.create(reserva=reserva, **servicio_data)
        return reserva

    def update(self, instance, validated_data):
        servicios_data = validated_data.pop('servicios_adicionales', None)
        # TODO: Recalcular costo si cambian los datos base
        instance = super().update(instance, validated_data)

        if servicios_data is not None:
            instance.servicios_adicionales.all().delete()
            for servicio_data in servicios_data:
                ReservaServicioAdicional.objects.create(reserva=instance, **servicio_data)

        return instance
