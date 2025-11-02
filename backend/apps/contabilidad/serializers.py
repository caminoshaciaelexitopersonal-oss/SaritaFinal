from rest_framework import serializers
from .models import ChartOfAccount, JournalEntry, Transaction
from decimal import Decimal

class ChartOfAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartOfAccount
        fields = ['id', 'codigo', 'nombre', 'naturaleza', 'permite_transacciones']
        read_only_fields = ('perfil',)

class TransactionReadSerializer(serializers.ModelSerializer):
    account = ChartOfAccountSerializer(read_only=True)
    class Meta:
        model = Transaction
        fields = ['id', 'account', 'debit', 'credit']

class JournalEntryReadSerializer(serializers.ModelSerializer):
    transactions = TransactionReadSerializer(many=True, read_only=True)
    class Meta:
        model = JournalEntry
        fields = ['id', 'entry_date', 'description', 'entry_type', 'transactions']

class TransactionWriteSerializer(serializers.Serializer):
    account_id = serializers.IntegerField()
    debit = serializers.DecimalField(max_digits=18, decimal_places=2, default=Decimal('0.00'))
    credit = serializers.DecimalField(max_digits=18, decimal_places=2, default=Decimal('0.00'))

    def validate(self, data):
        if data.get('debit', 0) > 0 and data.get('credit', 0) > 0:
            raise serializers.ValidationError("Débito y Crédito no pueden tener valor en la misma transacción.")
        if data.get('debit', 0) == 0 and data.get('credit', 0) == 0:
            raise serializers.ValidationError("La transacción debe tener un valor de débito o crédito.")
        return data

class JournalEntryWriteSerializer(serializers.ModelSerializer):
    transactions = TransactionWriteSerializer(many=True, min_length=2)

    class Meta:
        model = JournalEntry
        fields = ['entry_date', 'description', 'entry_type', 'transactions']
