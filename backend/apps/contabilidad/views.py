# backend/apps/contabilidad/views.py
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from .models import ChartOfAccount, JournalEntry, CostCenter
from .serializers import (
    ChartOfAccountReadSerializer, JournalEntryReadSerializer,
    JournalEntryWriteSerializer, CostCenterSerializer
)

# Un permiso personalizado para asegurar que el usuario es un prestador con perfil
class IsPrestadorConPerfil(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'perfil_prestador')

class PerfilDataMixin:
    """
    Mixin para filtrar querysets por el perfil del prestador
    y para inyectar el perfil en el contexto del serializador.
    """
    def get_queryset(self):
        # Filtra el queryset para devolver solo objetos del perfil del usuario
        return super().get_queryset().filter(perfil=self.request.user.perfil_prestador)

    def get_serializer_context(self):
        # Inyecta el perfil en el contexto para que el serializador lo use
        context = super().get_serializer_context()
        context['perfil'] = self.request.user.perfil_prestador
        return context

    def perform_create(self, serializer):
        # Asigna el perfil automáticamente al crear un objeto
        serializer.save(perfil=self.request.user.perfil_prestador)

class ChartOfAccountViewSet(PerfilDataMixin, viewsets.ModelViewSet):
    """API para el Plan de Cuentas (PUC) de un prestador."""
    queryset = ChartOfAccount.objects.all()
    serializer_class = ChartOfAccountReadSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorConPerfil]

class CostCenterViewSet(PerfilDataMixin, viewsets.ModelViewSet):
    """API para los Centros de Costo de un prestador."""
    queryset = CostCenter.objects.all()
    serializer_class = CostCenterSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorConPerfil]

    def get_queryset(self):
        """
        Asegura que el queryset esté filtrado por el perfil del usuario autenticado.
        """
        user = self.request.user
        if hasattr(user, 'perfil_prestador'):
            return self.queryset.filter(perfil=user.perfil_prestador)
        return self.queryset.none()

class JournalEntryViewSet(PerfilDataMixin, viewsets.ModelViewSet):
    """API para los Asientos Contables de un prestador."""
    queryset = JournalEntry.objects.select_related('user').prefetch_related('transactions__account').all()
    permission_classes = [permissions.IsAuthenticated, IsPrestadorConPerfil]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return JournalEntryWriteSerializer
        return JournalEntryReadSerializer

    def create(self, request, *args, **kwargs):
        """
        Personalización para inyectar el perfil del prestador en el contexto del serializador
        al momento de la creación.
        """
        # Adaptación: Pasamos el `request` completo al contexto del serializador
        # para que pueda acceder tanto a `user` como a `perfil_prestador`.
        context = self.get_serializer_context()
        context['request'] = request

        serializer = self.get_serializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        # El serializer ahora llama al servicio y crea todo.
        # `perform_create` ya no es necesario aquí para la creación.
        serializer.save()

        # Devolvemos el objeto creado usando el serializer de lectura
        read_serializer = JournalEntryReadSerializer(serializer.instance, context=self.get_serializer_context())
        headers = self.get_success_headers(read_serializer.data)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED, headers=headers)
