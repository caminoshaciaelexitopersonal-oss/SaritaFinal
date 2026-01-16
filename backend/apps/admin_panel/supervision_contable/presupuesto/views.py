from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.clientes.models import Presupuesto, PartidaPresupuestal, EjecucionPresupuestal
from .serializers import PresupuestoSerializer, PartidaPresupuestalSerializer, EjecucionPresupuestalSerializer

        if hasattr(obj, 'presupuesto'):
            return obj.presupuesto.perfil == request.user.perfil_prestador
        if hasattr(obj, 'partida'):
            return obj.partida.presupuesto.perfil == request.user.perfil_prestador
        return False

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class PresupuestoAdminViewSet(viewsets.ModelViewSet):
    serializer_class = PresupuestoSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return .objects.all()

    def perform_create(self, serializer):
        serializer.save(perfil=self.request.user.perfil_prestador)

class PartidaPresupuestalAdminViewSet(viewsets.ModelViewSet):
    serializer_class = PartidaPresupuestalSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return PartidaPresupuestal.objects.filter(presupuesto__perfil=self.request.user.perfil_prestador)

class EjecucionPresupuestalAdminViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EjecucionPresupuestalSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return EjecucionPresupuestal.objects.filter(partida__presupuesto__perfil=self.request.user.perfil_prestador)
