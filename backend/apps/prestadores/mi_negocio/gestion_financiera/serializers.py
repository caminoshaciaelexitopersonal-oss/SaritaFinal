# backend/apps/financiero/serializers.py
from rest_framework import serializers
from .models import *
from .services import create_cash_transaction_with_accounting
class BankAccountSerializer(serializers.ModelSerializer):
    class Meta: model = BankAccount; fields = '__all__'; read_only_fields = ['perfil', 'balance']
class CashTransactionSerializer(serializers.ModelSerializer):
    generate_journal_entry = serializers.BooleanField(write_only=True, default=False)
    debit_account_number = serializers.CharField(write_only=True, required=False)
    credit_account_number = serializers.CharField(write_only=True, required=False)
    class Meta: model = CashTransaction; fields = '__all__'; read_only_fields = ['perfil', 'journal_entry']
    def create(self, validated_data):
        return create_cash_transaction_with_accounting(perfil=self.context['request'].user.perfil_prestador, created_by=self.context['request'].user, **validated_data)
