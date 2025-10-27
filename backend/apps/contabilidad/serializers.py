# backend/apps/contabilidad/serializers.py
from rest_framework import serializers
from .models import CostCenter, Currency, ChartOfAccount, JournalEntry, Transaction
from .services import create_full_journal_entry

class CostCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCenter
        fields = ['id', 'name', 'description', 'perfil']
        read_only_fields = ['perfil']

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['code', 'name']

class ChartOfAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartOfAccount
        fields = ['id', 'account_number', 'name', 'account_type', 'is_active', 'parent', 'perfil']
        read_only_fields = ['perfil']

class TransactionSerializer(serializers.ModelSerializer):
    account_number = serializers.CharField(source='account.account_number', read_only=True)

    class Meta:
        model = Transaction
        fields = ['id', 'account', 'account_number', 'debit', 'credit', 'description']
        extra_kwargs = {
            'account': {'write_only': True},
        }

class WriteTransactionSerializer(serializers.Serializer):
    """
    Serializer para escribir transacciones anidadas.
    Recibe el número de cuenta en lugar del ID para facilitar la creación.
    """
    account_number = serializers.CharField(max_length=20)
    debit = serializers.DecimalField(max_digits=12, decimal_places=2, default=0)
    credit = serializers.DecimalField(max_digits=12, decimal_places=2, default=0)
    description = serializers.CharField(max_length=255, required=False, allow_blank=True)

class JournalEntrySerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True, read_only=True)
    transactions_data = WriteTransactionSerializer(many=True, write_only=True)
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)

    class Meta:
        model = JournalEntry
        fields = [
            'id', 'date', 'description', 'cost_center',
            'created_at', 'created_by', 'created_by_username',
            'transactions', 'transactions_data'
        ]
        read_only_fields = ['perfil', 'created_by']

    def create(self, validated_data):
        transactions_data = validated_data.pop('transactions_data')
        perfil = self.context['request'].user.perfil_prestador
        created_by = self.context['request'].user

        journal_entry = create_full_journal_entry(
            perfil=perfil,
            created_by=created_by,
            transactions_data=transactions_data,
            **validated_data
        )
        return journal_entry
