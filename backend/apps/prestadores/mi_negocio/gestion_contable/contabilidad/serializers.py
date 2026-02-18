# backend/apps/prestadores/mi_negocio/gestion_contable/serializers.py
from rest_framework import serializers
from .models import (
    PlanDeCuentas,
    Cuenta,
    PeriodoContable,
    AsientoContable,
    Transaccion,
)

class TransaccionSerializer(serializers.ModelSerializer):
    """
    Serializador para una transacción individual.
    """
    class Meta:
        model = Transaccion
        fields = ['id', 'cuenta', 'debit', 'credit', 'description']


class AsientoContableSerializer(serializers.ModelSerializer):
    """
    Serializador para un asiento contable.
    Incluye transacciones anidadas para proporcionar una vista completa.
    """
    transactions = TransaccionSerializer(many=True)
    creado_por = serializers.StringRelatedField()

    class Meta:
        model = AsientoContable
        fields = [
            'id',
            'periodo',
            'date',
            'description',
            'creado_por',
            'transactions',
        ]


class CuentaSerializer(serializers.ModelSerializer):
    """
    Serializador para una cuenta contable.
    Utiliza recursión para mostrar las sub-cuentas anidadas.
    """
    children = serializers.SerializerMethodField()

    class Meta:
        model = Cuenta
        fields = [
            'id',
            'name',
            'code',
            'account_type',
            'description',
            'saldo_inicial',
            'parent',
            'children',
        ]

    def get_children(self, obj):
        """ Retorna los hijos de la cuenta de forma recursiva. """
        return CuentaSerializer(obj.children.all(), many=True).data


class PlanDeCuentasSerializer(serializers.ModelSerializer):
    """
    Serializador para el Plan de Cuentas.
    Muestra las cuentas de nivel superior (aquellas sin padre).
    """
    cuentas = serializers.SerializerMethodField()

    class Meta:
        model = PlanDeCuentas
        fields = ['id', 'name', 'description', 'provider', 'cuentas']

    def get_cuentas(self, obj):
        """ Filtra para obtener solo las cuentas raíz. """
        cuentas_raiz = obj.cuentas.filter(parent__isnull=True)
        return CuentaSerializer(cuentas_raiz, many=True).data


class PeriodoContableSerializer(serializers.ModelSerializer):
    """
    Serializador para el Período Contable.
    """
    class Meta:
        model = PeriodoContable
        fields = ['id', 'name', 'start_date', 'end_date', 'is_closed', 'provider']
