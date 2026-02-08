from rest_framework import serializers
from apps.admin_plataforma.gestion_contable.contabilidad.models import (
    PlanDeCuentas, Cuenta, PeriodoContable, AsientoContable, Transaccion
)

class AdminPlanDeCuentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanDeCuentas
        fields = '__all__'
        read_only_fields = ['provider']

class AdminCuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = '__all__'

class AdminPeriodoContableSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodoContable
        fields = '__all__'
        read_only_fields = ['provider']

class AdminAsientoContableSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsientoContable
        fields = '__all__'
        read_only_fields = ['provider']
