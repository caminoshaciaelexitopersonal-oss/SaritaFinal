from rest_framework import serializers
from .models import CuentaBancaria, TransaccionBancaria
from apps.prestadores.mi_negocio.gestion_contable.contabilidad.serializers import ChartOfAccountSerializer

class CuentaBancariaSerializer(serializers.ModelSerializer):
    cuenta_contable_details = ChartOfAccountSerializer(source='cuenta_contable', read_only=True)

    class Meta:
        model = CuentaBancaria
        fields = [
            'id',
            'perfil',
            'banco',
            'numero_cuenta',
            'tipo_cuenta',
            'saldo_actual',
            'titular',
            'cuenta_contable',
            'cuenta_contable_details'
        ]
        read_only_fields = ('perfil', 'saldo_actual')


class TransaccionBancariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransaccionBancaria
        fields = [
            'id',
            'cuenta',
            'fecha',
            'tipo',
            'monto',
            'descripcion',
            'creado_por',
            'creado_en'
        ]
        read_only_fields = ('creado_por',)
