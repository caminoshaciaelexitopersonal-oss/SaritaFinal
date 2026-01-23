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
        fields = ['id', 'cuenta', 'debito', 'credito', 'descripcion']


class AsientoContableSerializer(serializers.ModelSerializer):
    """
    Serializador para un asiento contable.
    Incluye transacciones anidadas para proporcionar una vista completa.
    """
    transacciones = TransaccionSerializer(many=True)
    creado_por = serializers.StringRelatedField()

    class Meta:
        model = AsientoContable
        fields = [
            'id',
            'periodo',
            'fecha',
            'descripcion',
            'creado_por',
            'transacciones',
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
            'nombre',
            'codigo',
            'tipo',
            'descripcion',
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
        fields = ['id', 'nombre', 'descripcion', 'provider', 'cuentas']

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
        fields = ['id', 'nombre', 'fecha_inicio', 'fecha_fin', 'cerrado', 'provider']
