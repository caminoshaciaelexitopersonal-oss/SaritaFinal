from rest_framework import viewsets, permissions
from .models import ChartOfAccount, JournalEntry
from .serializers import (
    ChartOfAccountSerializer,
    JournalEntryReadSerializer,
    JournalEntryWriteSerializer,
)
from apps.mi_negocio.permissions import IsPrestadorOwner # Permiso reutilizable

class ChartOfAccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint para el Plan de Cuentas (PUC) de un prestador.
    """
    serializer_class = ChartOfAccountSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        """
        Esta vista solo debe devolver las cuentas del perfil del usuario autenticado.
        """
        return ChartOfAccount.objects.filter(perfil=self.request.user.perfil_prestador)

    def perform_create(self, serializer):
        """
        Asigna automáticamente el perfil del prestador al crear una nueva cuenta.
        """
        serializer.save(perfil=self.request.user.perfil_prestador)

class JournalEntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint para los Asientos Contables de un prestador.
    """
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        """
        Esta vista solo debe devolver los asientos del perfil del usuario autenticado.
        """
        return JournalEntry.objects.filter(perfil=self.request.user.perfil_prestador)

    def get_serializer_class(self):
        """
        Usa un serializador diferente para leer y para escribir datos.
        """
        if self.action in ['create', 'update', 'partial_update']:
            return JournalEntryWriteSerializer
        return JournalEntryReadSerializer

    def perform_create(self, serializer):
        """
        Asigna automáticamente el perfil y el usuario al crear un nuevo asiento.
        """
        # Aquí iría la lógica del `services.py` para crear el asiento de forma atómica.
        # Por ahora, lo creamos directamente para validar la estructura.
        serializer.save(perfil=self.request.user.perfil_prestador, usuario=self.request.user)
