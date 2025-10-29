# backend/apps/financiera/serializers.py
from rest_framework import serializers
from .models import BankAccount, CashTransaction

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = '__all__'
        read_only_fields = ('perfil',)

class CashTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashTransaction
        fields = '__all__'
        read_only_fields = ('perfil', 'created_by')

    def validate_bank_account(self, value):
        """
        Asegurarse de que la cuenta bancaria pertenezca al perfil del usuario.
        """
        if value.perfil != self.context['request'].user.perfil_prestador:
            raise serializers.ValidationError("La cuenta bancaria no pertenece a su negocio.")
        return value
