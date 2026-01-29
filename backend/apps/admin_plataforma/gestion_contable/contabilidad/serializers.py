from rest_framework import serializers
from apps.prestadores.mi_negocio.gestion_contable.contabilidad.models import (
    PlanDeCuentas, Cuenta, PeriodoContable, AsientoContable, Transaccion
)

class PlanDeCuentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanDeCuentas
        fields = '__all__'
        read_only_fields = ['provider']

class CuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = '__all__'

class PeriodoContableSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodoContable
        fields = '__all__'
        read_only_fields = ['provider']

class AsientoContableSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsientoContable
        fields = '__all__'
        read_only_fields = ['provider']
