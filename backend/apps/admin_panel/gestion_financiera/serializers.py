from rest_framework import serializers
from apps.prestadores.mi_negocio.gestion_financiera.models import CuentaBancaria, OrdenPago

class CuentaBancariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuentaBancaria
        fields = '__all__'

class OrdenPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenPago
        fields = '__all__'
