# backend/apps/financiero/serializers.py
from rest_framework import serializers
from .models import BankAccount, CashTransaction
from .services import create_cash_transaction_with_accounting

class BankAccountSerializer(serializers.ModelSerializer):
    currency_code = serializers.CharField(source='currency.code')

    class Meta:
        model = BankAccount
        fields = [
            'id', 'bank_name', 'account_number', 'account_holder',
            'account_type', 'currency_code', 'balance', 'is_active',
            'linked_account', 'perfil'
        ]
        read_only_fields = ['perfil', 'balance']

class CashTransactionSerializer(serializers.ModelSerializer):
    bank_account_name = serializers.CharField(source='bank_account.__str__', read_only=True)
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)

    # Campos para la creación del asiento contable
    debit_account_number = serializers.CharField(write_only=True, required=False)
    credit_account_number = serializers.CharField(write_only=True, required=False)
    generate_journal_entry = serializers.BooleanField(write_only=True, default=False)

    class Meta:
        model = CashTransaction
        fields = [
            'id', 'bank_account', 'bank_account_name', 'transaction_type',
            'amount', 'date', 'description', 'reference', 'created_at',
            'created_by', 'created_by_username', 'journal_entry',
            'debit_account_number', 'credit_account_number', 'generate_journal_entry'
        ]
        read_only_fields = ['perfil', 'created_by', 'journal_entry']

    def validate(self, data):
        if data.get('generate_journal_entry'):
            if not data.get('debit_account_number') or not data.get('credit_account_number'):
                raise serializers.ValidationError(
                    "Se requieren 'debit_account_number' y 'credit_account_number' para generar el asiento contable."
                )
        return data

    def create(self, validated_data):
        perfil = self.context['request'].user.perfil_prestador
        created_by = self.context['request'].user

        generate_journal_entry = validated_data.pop('generate_journal_entry', False)
        debit_account_number = validated_data.pop('debit_account_number', None)
        credit_account_number = validated_data.pop('credit_account_number', None)

        cash_transaction = create_cash_transaction_with_accounting(
            perfil=perfil,
            created_by=created_by,
            generate_journal_entry=generate_journal_entry,
            debit_account_number=debit_account_number,
            credit_account_number=credit_account_number,
            **validated_data
        )
        return cash_transaction
