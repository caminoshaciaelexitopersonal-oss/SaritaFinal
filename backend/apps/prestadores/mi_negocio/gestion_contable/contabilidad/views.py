from rest_framework import viewsets, permissions
from .models import ChartOfAccount, JournalEntry, CostCenter
from .serializers import ChartOfAccountSerializer, JournalEntrySerializer, CostCenterSerializer
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.permissions import IsOwner

class ChartOfAccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint para el Plan de Cuentas. Es de solo lectura ya que
    generalmente es gestionado por administradores del sistema.
    """
    queryset = ChartOfAccount.objects.all()
    serializer_class = ChartOfAccountSerializer
    permission_classes = [permissions.IsAuthenticated] # Solo usuarios autenticados pueden ver el plan
    http_method_names = ['get'] # Solo permitir peticiones GET

class CostCenterViewSet(viewsets.ModelViewSet):
    """
    API endpoint para Centros de Costo.
    """
    serializer_class = CostCenterSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        # Filtrar por el perfil del usuario autenticado
        return CostCenter.objects.filter(perfil=self.request.user.perfil_prestador)

    def perform_create(self, serializer):
        # Asignar automáticamente el perfil del usuario al crear
        serializer.save(perfil=self.request.user.perfil_prestador)


class JournalEntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint para Asientos Contables.
    """
    serializer_class = JournalEntrySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        # Filtrar por el perfil del usuario autenticado
        return JournalEntry.objects.filter(perfil=self.request.user.perfil_prestador)

    def perform_create(self, serializer):
        # Asignar automáticamente el perfil y el usuario al crear
        serializer.save(
            perfil=self.request.user.perfil_prestador,
            user=self.request.user
        )
