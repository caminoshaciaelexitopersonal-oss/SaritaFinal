# backend/apps/financiera/serializers.py
from rest_framework import serializers
from .models import BankAccount, CashTransaction

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = [
            'id', 'bank_name', 'account_number', 'account_holder',
            'account_type', 'balance', 'is_active', 'linked_account'
        ]
        read_only_fields = ['perfil']

class CashTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashTransaction
        fields = [
            'id', 'bank_account', 'transaction_type', 'amount', 'date',
            'description', 'reference', 'created_at', 'journal_entry'
        ]
        read_only_fields = ['perfil', 'created_by']

    def validate_bank_account(self, value):
        """
        Check that the bank account belongs to the user's profile.
        """
        user = self.context['request'].user
        if not hasattr(user, 'perfil_prestador') or value.perfil != user.perfil_prestador:
            raise serializers.ValidationError("La cuenta bancaria seleccionada no es válida para este perfil.")
        return value
