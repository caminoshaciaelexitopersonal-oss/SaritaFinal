from rest_framework import serializers
from .models import BankAccount, CashTransaction
from apps.prestadores.mi_negocio.gestion_contable.contabilidad.serializers import JournalEntryReadSerializer

# --- SERIALIZADORES DE SOLO LECTURA ---

class BankAccountReadSerializer(serializers.ModelSerializer):
    linked_account_code = serializers.CharField(source='linked_account.code', read_only=True)

    class Meta:
        model = BankAccount
        fields = ['id', 'name', 'account_number', 'bank_name', 'linked_account_code', 'is_active']

class CashTransactionReadSerializer(serializers.ModelSerializer):
    bank_account_name = serializers.CharField(source='bank_account.name', read_only=True)
    journal_entry = JournalEntryReadSerializer(read_only=True)

    class Meta:
        model = CashTransaction
        fields = [
            'id', 'transaction_date', 'description', 'amount', 'transaction_type',
            'status', 'bank_account_name', 'journal_entry'
        ]

# --- SERIALIZADORES DE ESCRITURA ---

class BankAccountWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ['name', 'account_number', 'bank_name', 'linked_account']

    def validate(self, data):
        data['perfil'] = self.context['request'].user.perfil_prestador
        return data

class CashTransactionWriteSerializer(serializers.Serializer):
    bank_account_id = serializers.IntegerField()
    transaction_date = serializers.DateField()
    description = serializers.CharField(max_length=512)
    amount = serializers.DecimalField(max_digits=18, decimal_places=2)
    contra_account_code = serializers.CharField(max_length=20)

    def create(self, validated_data):
        from .services import record_cash_movement

        try:
            user = self.context['request'].user
            bank_account = BankAccount.objects.get(
                id=validated_data['bank_account_id'],
                perfil=user.perfil_prestador
            )

            cash_transaction = record_cash_movement(
                user=user,
                bank_account=bank_account,
                **{k: v for k, v in validated_data.items() if k != 'bank_account_id'}
            )
            return cash_transaction
        except BankAccount.DoesNotExist:
            raise serializers.ValidationError("La cuenta bancaria especificada no existe o no pertenece a su perfil.")
        except ValueError as e:
            raise serializers.ValidationError(str(e))
