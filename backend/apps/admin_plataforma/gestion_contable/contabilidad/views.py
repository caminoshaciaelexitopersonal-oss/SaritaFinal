from rest_framework import viewsets, permissions
from api.permissions import IsSuperAdmin
from apps.admin_plataforma.mixins import SystemicERPViewSetMixin
from apps.prestadores.mi_negocio.gestion_contable.contabilidad.models import (
    PlanDeCuentas, Cuenta, PeriodoContable, AsientoContable, Transaccion
)
from .serializers import (
    PlanDeCuentasSerializer, CuentaSerializer,
    PeriodoContableSerializer, AsientoContableSerializer
)

class PlanDeCuentasViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    queryset = PlanDeCuentas.objects.all()
    serializer_class = PlanDeCuentasSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def perform_create(self, serializer):
        from apps.admin_plataforma.services.gestion_plataforma_service import GestionPlataformaService
        perfil_gobierno = GestionPlataformaService.get_perfil_gobierno()
        serializer.save(provider=perfil_gobierno)

class CuentaViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

class PeriodoContableViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    queryset = PeriodoContable.objects.all()
    serializer_class = PeriodoContableSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

class AsientoContableViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    queryset = AsientoContable.objects.all()
    serializer_class = AsientoContableSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]
