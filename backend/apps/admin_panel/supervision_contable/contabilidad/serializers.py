from rest_framework import serializers
from .models import ChartOfAccount, JournalEntry, Transaction, CostCenter

class ChartOfAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartOfAccount
        fields = ['code', 'name', 'nature', 'allows_transactions']

class CostCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCenter
        fields = ['id', 'perfil', 'code', 'name']
        read_only_fields = ('perfil',)

class TransactionSerializer(serializers.ModelSerializer):
    account_details = ChartOfAccountSerializer(source='account', read_only=True)

    class Meta:
        model = Transaction
        fields = ['id', 'account', 'debit', 'credit', 'cost_center', 'account_details']


class JournalEntrySerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True)
    perfil = serializers.PrimaryKeyRelatedField(read_only=True) # El perfil se tomará del usuario autenticado

    class Meta:
        model = JournalEntry
        fields = [
            'id',
            'perfil',
            'entry_date',
            'description',
            'entry_type',
            'user',
            'origin_document',
            'created_at',
            'transactions'
        ]
        read_only_fields = ('user', 'perfil') # Estos campos se gestionarán internamente

    def validate(self, data):
        # La validación se aplica tanto a la creación como a la actualización
        transactions = data.get('transactions')
        if not transactions:
            raise serializers.ValidationError("Un asiento contable debe tener al menos una transacción.")

        total_debit = sum(item.get('debit', 0) for item in transactions)
        total_credit = sum(item.get('credit', 0) for item in transactions)

        if total_debit != total_credit:
            raise serializers.ValidationError(f"El asiento está desbalanceado. Débitos: {total_debit}, Créditos: {total_credit}")

        if total_debit == 0 and total_credit == 0:
            raise serializers.ValidationError("El asiento contable no puede tener un valor total de cero.")

        return data

    def create(self, validated_data):
        transactions_data = validated_data.pop('transactions')
        journal_entry = JournalEntry.objects.create(**validated_data)
        for transaction_data in transactions_data:
            Transaction.objects.create(journal_entry=journal_entry, **transaction_data)
        return journal_entry

    def update(self, instance, validated_data):
        transactions_data = validated_data.pop('transactions', None)

        instance.entry_date = validated_data.get('entry_date', instance.entry_date)
        instance.description = validated_data.get('description', instance.description)
        instance.entry_type = validated_data.get('entry_type', instance.entry_type)
        instance.save()

        if transactions_data is not None:
            # Eliminar transacciones antiguas y crear las nuevas
            instance.transactions.all().delete()
            for transaction_data in transactions_data:
                Transaction.objects.create(journal_entry=instance, **transaction_data)

        return instance
