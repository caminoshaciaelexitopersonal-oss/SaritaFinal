# backend/apps/contabilidad/serializers.py
from rest_framework import serializers
from .models import ChartOfAccount, JournalEntry, Transaction, CostCenter
# Se comenta la dependencia a 'Project' que aún no existe
# from projects.models import Project

# --- SERIALIZERS DE SOLO LECTURA (PARA MOSTRAR DATOS) ---
class ChartOfAccountReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChartOfAccount
        fields = ['id', 'code', 'name', 'nature', 'allows_transactions']

class CostCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCenter
        fields = ['id', 'code', 'name']

class TransactionReadSerializer(serializers.ModelSerializer):
    account = ChartOfAccountReadSerializer(read_only=True)
    cost_center_code = serializers.CharField(source='cost_center.code', allow_null=True)
    # project_code = serializers.CharField(source='project.code', allow_null=True)

    class Meta:
        model = Transaction
        fields = ['id', 'account', 'debit', 'credit', 'cost_center_code'] # Removido 'project_code'

class JournalEntryReadSerializer(serializers.ModelSerializer):
    transactions = TransactionReadSerializer(many=True, read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = JournalEntry
        fields = ['id', 'entry_date', 'description', 'entry_type', 'user_username', 'created_at', 'transactions']


# --- SERIALIZERS DE ESCRITURA (PARA CREAR DATOS) ---
class TransactionWriteSerializer(serializers.Serializer):
    account_code = serializers.CharField(max_length=20)
    debit = serializers.DecimalField(max_digits=18, decimal_places=2, default=0)
    credit = serializers.DecimalField(max_digits=18, decimal_places=2, default=0)
    cost_center_code = serializers.CharField(max_length=20, required=False, allow_null=True)
    # project_code = serializers.CharField(max_length=50, required=False, allow_null=True)

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
            # Se inyecta el usuario del request actual, garantizando la autoría.
            user = self.context['request'].user

            # **ADAPTACIÓN CLAVE**: Obtenemos el perfil directamente desde el usuario autenticado.
            perfil = self.context['request'].user.perfil_prestador

            # Se llama al servicio de negocio, manteniendo el serializer limpio.
            journal_entry = create_full_journal_entry(
                user=user,
                perfil=perfil,
                entry_date=validated_data['entry_date'],
                description=validated_data['description'],
                entry_type=validated_data['entry_type'],
                transactions_data=validated_data['transactions']
            )
            return journal_entry
        except ValueError as e:
            # Propaga errores de negocio (partida doble, cuenta no válida) como errores de API.
            raise serializers.ValidationError(str(e))
        except AttributeError:
             raise serializers.ValidationError("No se pudo determinar el perfil del negocio para esta operación.")
