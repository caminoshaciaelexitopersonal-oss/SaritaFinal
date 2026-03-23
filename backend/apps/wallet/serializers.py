from rest_framework import serializers
from .models import WalletAccount, WalletTransaction

class WalletAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletAccount
        fields = '__all__'
        read_only_fields = ('balance', 'status')

class WalletTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletTransaction
        fields = '__all__'
