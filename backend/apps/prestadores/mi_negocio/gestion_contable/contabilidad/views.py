from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import ChartOfAccount, JournalEntry, CostCenter
from .serializers import (
    ChartOfAccountReadSerializer,
    JournalEntryReadSerializer,
    JournalEntryWriteSerializer,
    CostCenterSerializer
)
from apps.prestadores.mi_negocio.permissions import IsPrestadorOwner

class ChartOfAccountViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ChartOfAccountReadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Asumiendo que el Plan de Cuentas es global, no filtrado por perfil.
        # Si fuese específico por perfil, aquí iría el filtro.
        return ChartOfAccount.objects.all()

class JournalEntryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return JournalEntryWriteSerializer
        return JournalEntryReadSerializer

    def get_queryset(self):
        return JournalEntry.objects.filter(
            perfil=self.request.user.perfil_prestador
        ).select_related(
            'user'
        ).prefetch_related(
            'transactions__account',
            'transactions__cost_center'
            # 'transactions__project' # TODO: Habilitar
        ).all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Después de guardar, retornamos el resultado usando el ReadSerializer
        read_serializer = JournalEntryReadSerializer(serializer.instance)
        headers = self.get_success_headers(read_serializer.data)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class CostCenterViewSet(viewsets.ModelViewSet):
    serializer_class = CostCenterSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        return CostCenter.objects.filter(perfil=self.request.user.perfil_prestador)
