from rest_framework import serializers
from django.apps import apps

Account = apps.get_model('core_erp', 'Account')

class PlanCuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'code', 'name', 'type', 'parent_account', 'initial_balance', 'is_active', 'ifrs_mapping']
        read_only_fields = ['id']

    def validate_code(self, value):
        # PUC 6-digit validation
        if len(value) != 6 or not value.isdigit():
            raise serializers.ValidationError('Código PUC debe ser 6 dígitos numéricos.')
        return value

    def create(self, validated_data):
        # Tenant auto-set
        request = self.context.get('request')
        validated_data['tenant'] = request.tenant if request else None
        return super().create(validated_data)
