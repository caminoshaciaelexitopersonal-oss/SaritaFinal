from rest_framework import viewsets, permissions
from apps.prestadores.mi_negocio.gestion_contable.nomina.models import Empleado, Contrato, Planilla, ConceptoNomina
from .serializers import EmpleadoSerializer, ContratoSerializer, PlanillaSerializer, ConceptoNominaSerializer
from apps.admin_plataforma.mixins import SystemicERPViewSetMixin
from api.permissions import IsSuperAdmin

class IsPrestadorOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'perfil'):
            return obj.perfil == request.user.perfil_prestador
        if hasattr(obj, 'empleado') and hasattr(obj.empleado, 'perfil'):
             return obj.empleado.perfil == request.user.perfil_prestador
        return False

class EmpleadoViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    serializer_class = EmpleadoSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def get_queryset(self):
        return Empleado.objects.filter(perfil=self.request.user.perfil_prestador)

class ContratoViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    serializer_class = ContratoSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def get_queryset(self):
        return Contrato.objects.filter(empleado__perfil=self.request.user.perfil_prestador)

class PlanillaViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    serializer_class = PlanillaSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def get_queryset(self):
        return Planilla.objects.filter(perfil=self.request.user.perfil_prestador)

class ConceptoNominaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ConceptoNomina.objects.all()
    serializer_class = ConceptoNominaSerializer
    permission_classes = [permissions.IsAuthenticated]
