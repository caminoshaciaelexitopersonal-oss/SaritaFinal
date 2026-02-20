from rest_framework import viewsets, permissions
from api.permissions import IsSuperAdmin
from apps.admin_plataforma.mixins import SystemicERPViewSetMixin
from apps.admin_plataforma.gestion_contable.contabilidad.models import (
    AdminChartOfAccounts, AdminAccount, AdminFiscalPeriod, AdminJournalEntry, AdminAccountingTransaction
)
from .serializers import (
    AdminPlanDeCuentasSerializer, AdminCuentaSerializer,
    AdminPeriodoContableSerializer, AdminAsientoContableSerializer
)
from apps.core_erp.accounting_engine import AccountingEngine

class PlanDeCuentasViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    queryset = AdminChartOfAccounts.objects.all()
    serializer_class = AdminPlanDeCuentasSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def perform_create(self, serializer):
        from apps.admin_plataforma.services.gestion_plataforma_service import GestionPlataformaService
        perfil_gobierno = GestionPlataformaService.get_perfil_gobierno_context()
        serializer.save(provider=perfil_gobierno)

class CuentaViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    queryset = AdminAccount.objects.all()
    serializer_class = AdminCuentaSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

class PeriodoContableViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    queryset = AdminFiscalPeriod.objects.all()
    serializer_class = AdminPeriodoContableSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

class AsientoContableViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    queryset = AdminJournalEntry.objects.all()
    serializer_class = AdminAsientoContableSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def perform_create(self, serializer):
        entry = serializer.save()
        AccountingEngine.post_journal_entry(entry)
