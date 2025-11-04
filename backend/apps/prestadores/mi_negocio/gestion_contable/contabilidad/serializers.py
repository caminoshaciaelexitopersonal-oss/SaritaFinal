from rest_framework import serializers
from .models import ChartOfAccount, JournalEntry, Transaction, CostCenter

# --- SERIALIZADORES DE SOLO LECTURA ---

class ChartOfAccountReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartOfAccount
        fields = ['code', 'name', 'nature']

class TransactionReadSerializer(serializers.ModelSerializer):
    account = ChartOfAccountReadSerializer(read_only=True)
    cost_center_code = serializers.CharField(source='cost_center.code', allow_null=True)
    # project_code = serializers.CharField(source='project.code', allow_null=True) # TODO: Habilitar

    class Meta:
        model = Transaction
        fields = ['id', 'account', 'debit', 'credit', 'cost_center_code'] #, 'project_code']

class JournalEntryReadSerializer(serializers.ModelSerializer):
    transactions = TransactionReadSerializer(many=True, read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = JournalEntry
        fields = ['id', 'entry_date', 'description', 'entry_type', 'user_username', 'created_at', 'transactions']

# --- SERIALIZADORES DE ESCRITURA ---

class TransactionWriteSerializer(serializers.Serializer):
    account_code = serializers.CharField(max_length=20)
    debit = serializers.DecimalField(max_digits=18, decimal_places=2, default=0)
    credit = serializers.DecimalField(max_digits=18, decimal_places=2, default=0)
    cost_center_code = serializers.CharField(max_length=20, required=False, allow_null=True)
    # project_code = serializers.CharField(max_length=50, required=False, allow_null=True) # TODO: Habilitar

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

    def create(self, validated_data):
        from .services import create_full_journal_entry

        try:
            user = self.context['request'].user
            perfil = user.perfil_prestador

            journal_entry = create_full_journal_entry(
                perfil=perfil,
                user=user,
                entry_date=validated_data['entry_date'],
                description=validated_data['description'],
                entry_type=validated_data['entry_type'],
                transactions_data=validated_data['transactions']
            )
            return journal_entry
        except ValueError as e:
            raise serializers.ValidationError(str(e))

# --- OTROS SERIALIZADORES ---
class CostCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCenter
        fields = ['id', 'code', 'name']

    def validate(self, data):
        # Asegurar que el perfil se asigne automáticamente
        if 'request' in self.context:
            data['perfil'] = self.context['request'].user.perfil_prestador
        return data
