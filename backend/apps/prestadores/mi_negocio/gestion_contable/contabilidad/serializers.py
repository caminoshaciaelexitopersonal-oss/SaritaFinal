from rest_framework import serializers
from .models import CostCenter, ChartOfAccount, Transaction, JournalEntry

class CostCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCenter
        fields = ['id', 'code', 'name']

    def validate(self, data):
        data['perfil'] = self.context['request'].user.perfil_prestador
        return data

class ChartOfAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartOfAccount
        fields = ['code', 'name', 'nature', 'allows_transactions']

class TransactionSerializer(serializers.ModelSerializer):
    account_code = serializers.CharField(source='account.code', read_only=True)
    cost_center_code = serializers.CharField(source='cost_center.code', required=False, allow_null=True)

    class Meta:
        model = Transaction
        fields = ['id', 'account', 'account_code', 'debit', 'credit', 'cost_center', 'cost_center_code']
        extra_kwargs = {
            'account': {'write_only': True},
            'cost_center': {'write_only': True, 'required': False, 'allow_null': True},
        }

class JournalEntrySerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = JournalEntry
        fields = ['id', 'entry_date', 'description', 'entry_type', 'user', 'transactions', 'created_at']
        read_only_fields = ('created_at',)

    def create(self, validated_data):
        transactions_data = validated_data.pop('transactions')
        validated_data['perfil'] = self.context['request'].user.perfil_prestador
        journal_entry = JournalEntry.objects.create(**validated_data)
        for transaction_data in transactions_data:
            Transaction.objects.create(journal_entry=journal_entry, **transaction_data)
        return journal_entry

    def validate(self, data):
        debit_total = sum(t.get('debit', 0) for t in data['transactions'])
        credit_total = sum(t.get('credit', 0) for t in data['transactions'])
        if debit_total != credit_total:
            raise serializers.ValidationError("El total de débitos y créditos debe ser igual.")
        return data
