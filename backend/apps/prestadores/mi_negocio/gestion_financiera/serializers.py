from rest_framework import serializers
from .models import CuentaBancaria, OrdenPago

class CuentaBancariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuentaBancaria
        fields = '__all__'

class OrdenPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenPago
        fields = '__all__'
