from rest_framework import serializers
from .models import BankAccount, CashTransaction

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ['id', 'nombre', 'numero_cuenta', 'nombre_banco', 'cuenta_contable_asociada', 'esta_activa']
        read_only_fields = ('perfil',)

class CashTransactionSerializer(serializers.ModelSerializer):
    cuenta_bancaria = BankAccountSerializer(read_only=True)
    class Meta:
        model = CashTransaction
        fields = ['id', 'cuenta_bancaria', 'fecha_transaccion', 'descripcion', 'monto', 'tipo_transaccion']
        read_only_fields = ('perfil', 'asiento_contable')
