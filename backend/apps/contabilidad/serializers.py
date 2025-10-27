# backend/apps/contabilidad/serializers.py
from rest_framework import serializers
from .models import *
from .services import create_full_journal_entry
class CurrencySerializer(serializers.ModelSerializer):
    class Meta: model = Currency; fields = '__all__'
class ChartOfAccountSerializer(serializers.ModelSerializer):
    class Meta: model = ChartOfAccount; fields = '__all__'; read_only_fields = ['perfil']
class TransactionSerializer(serializers.ModelSerializer):
    class Meta: model = Transaction; fields = '__all__'
class WriteTransactionSerializer(serializers.Serializer):
    account_number = serializers.CharField(); debit = serializers.DecimalField(max_digits=12, decimal_places=2, default=0); credit = serializers.DecimalField(max_digits=12, decimal_places=2, default=0)
class JournalEntrySerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True, read_only=True)
    transactions_data = WriteTransactionSerializer(many=True, write_only=True)
    class Meta: model = JournalEntry; fields = '__all__'; read_only_fields = ['perfil']
    def create(self, validated_data):
        return create_full_journal_entry(perfil=self.context['request'].user.perfil_prestador, created_by=self.context['request'].user, **validated_data)
