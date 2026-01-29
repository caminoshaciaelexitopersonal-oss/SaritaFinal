from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from apps.admin_plataforma.gestion_contable.presupuesto.models import Presupuesto, PartidaPresupuestal, EjecucionPresupuestal
from .serializers import PresupuestoSerializer, PartidaPresupuestalSerializer, EjecucionPresupuestalSerializer
from apps.admin_plataforma.mixins import SystemicERPViewSetMixin
from api.permissions import IsSuperAdmin

class IsPrestadorOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'perfil'):
            return obj.perfil == request.user.perfil_prestador
        if hasattr(obj, 'presupuesto'):
            return obj.presupuesto.perfil == request.user.perfil_prestador
        if hasattr(obj, 'partida'):
            return obj.partida.presupuesto.perfil == request.user.perfil_prestador
        return False

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class PresupuestoViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    serializer_class = PresupuestoSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return Presupuesto.objects.filter(perfil=self.request.user.perfil_prestador)

    def perform_create(self, serializer):
        serializer.save(perfil=self.request.user.perfil_prestador)

class PartidaPresupuestalViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    serializer_class = PartidaPresupuestalSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return PartidaPresupuestal.objects.filter(presupuesto__perfil=self.request.user.perfil_prestador)

class EjecucionPresupuestalViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EjecucionPresupuestalSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return EjecucionPresupuestal.objects.filter(partida__presupuesto__perfil=self.request.user.perfil_prestador)
