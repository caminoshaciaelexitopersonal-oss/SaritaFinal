# backend/apps/contabilidad/views.py
from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from .models import CostCenter, Currency, ChartOfAccount, JournalEntry
from .serializers import (
    CostCenterSerializer, CurrencySerializer, ChartOfAccountSerializer,
    JournalEntrySerializer
)

class IsOwnerOfPerfil(permissions.BasePermission):
    """
    Permiso para verificar que el objeto pertenece al perfil del usuario autenticado.
    """
    def has_object_permission(self, request, view, obj):
        # El perfil se obtiene del objeto mismo
        if hasattr(obj, 'perfil'):
            return obj.perfil == request.user.perfil_prestador
        # Para modelos sin perfil (como Currency), se permite el acceso
        return True

class ContabilidadBaseViewSet(viewsets.ModelViewSet):
    """
    ViewSet base para los modelos de contabilidad.
    Filtra automáticamente el queryset para que solo devuelva objetos
    pertenecientes al perfil del usuario autenticado.
    """
    permission_classes = [permissions.IsAuthenticated, IsOwnerOfPerfil]

    def get_queryset(self):
        # Asegurarse de que el usuario tiene un perfil de prestador
        try:
            perfil = self.request.user.perfil_prestador
        except AttributeError:
            raise PermissionDenied("El usuario no tiene un perfil de prestador asociado.")

        # Filtrar el queryset por el perfil del usuario
        return self.queryset.filter(perfil=perfil)

    def perform_create(self, serializer):
        # Asignar automáticamente el perfil del usuario al crear un objeto
        try:
            perfil = self.request.user.perfil_prestador
            serializer.save(perfil=perfil)
        except AttributeError:
            raise PermissionDenied("No se puede crear el objeto sin un perfil de prestador.")

class CostCenterViewSet(ContabilidadBaseViewSet):
    queryset = CostCenter.objects.all()
    serializer_class = CostCenterSerializer

class ChartOfAccountViewSet(ContabilidadBaseViewSet):
    queryset = ChartOfAccount.objects.all().order_by('account_number')
    serializer_class = ChartOfAccountSerializer

class JournalEntryViewSet(ContabilidadBaseViewSet):
    queryset = JournalEntry.objects.all().prefetch_related('transactions', 'transactions__account').order_by('-date')
    serializer_class = JournalEntrySerializer

    def perform_create(self, serializer):
        # La lógica de creación ya está en el serializador, que extrae el perfil del request.
        # Solo necesitamos pasar el usuario que crea el asiento.
        serializer.save(created_by=self.request.user)

class CurrencyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para monedas. Es de solo lectura y accesible por cualquier usuario autenticado,
    ya que no está ligado a un perfil específico.
    """
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [permissions.IsAuthenticated]
