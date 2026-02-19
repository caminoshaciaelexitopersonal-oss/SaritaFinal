from rest_framework import serializers
from apps.admin_plataforma.gestion_contable.contabilidad.models import (
    AdminChartOfAccounts, AdminAccount, AdminFiscalPeriod, AdminJournalEntry, AdminAccountingTransaction
)

class AdminPlanDeCuentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminChartOfAccounts
        fields = '__all__'
        read_only_fields = ['provider']

class AdminCuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminAccount
        fields = '__all__'

class AdminPeriodoContableSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminFiscalPeriod
        fields = '__all__'
        read_only_fields = ['provider']

class AdminAsientoContableSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminJournalEntry
        fields = '__all__'
        read_only_fields = ['provider']
