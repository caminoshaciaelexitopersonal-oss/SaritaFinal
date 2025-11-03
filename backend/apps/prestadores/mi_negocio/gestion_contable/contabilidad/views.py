from rest_framework import viewsets, permissions
from .models import CostCenter, ChartOfAccount, JournalEntry
from .serializers import CostCenterSerializer, ChartOfAccountSerializer, JournalEntrySerializer

class IsPrestadorOwner(permissions.BasePermission):
    """
    Permiso para permitir solo a los dueños de los objetos (perfil) verlos y editarlos.
    """
    def has_object_permission(self, request, view, obj):
        return obj.perfil == request.user.perfil_prestador

class CostCenterViewSet(viewsets.ModelViewSet):
    serializer_class = CostCenterSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        return CostCenter.objects.filter(perfil=self.request.user.perfil_prestador)

class ChartOfAccountViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Este ViewSet es de solo lectura ya que el plan de cuentas es estándar
    y no debería ser modificado por los usuarios.
    """
    queryset = ChartOfAccount.objects.all()
    serializer_class = ChartOfAccountSerializer
    permission_classes = [permissions.IsAuthenticated]

class JournalEntryViewSet(viewsets.ModelViewSet):
    serializer_class = JournalEntrySerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        return JournalEntry.objects.filter(perfil=self.request.user.perfil_prestador)
