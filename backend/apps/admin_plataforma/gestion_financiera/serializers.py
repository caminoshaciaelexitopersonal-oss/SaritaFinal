from rest_framework import serializers
from apps.prestadores.mi_negocio.gestion_financiera.models import CuentaBancaria, OrdenPago

class CuentaBancariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuentaBancaria
        fields = '__all__'
        read_only_fields = ['perfil_ref_id']

class OrdenPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenPago
        fields = '__all__'
