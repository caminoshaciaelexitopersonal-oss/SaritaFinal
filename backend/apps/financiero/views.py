from rest_framework import viewsets, permissions
from .models import BankAccount, CashTransaction
from .serializers import BankAccountSerializer, CashTransactionSerializer
from apps.mi_negocio.permissions import IsPrestadorOwner

class BankAccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint para las Cuentas Bancarias de un prestador.
    """
    serializer_class = BankAccountSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        return BankAccount.objects.filter(perfil=self.request.user.perfil_prestador)

    def perform_create(self, serializer):
        serializer.save(perfil=self.request.user.perfil_prestador)

class CashTransactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint para los Movimientos de Tesorería de un prestador.
    """
    serializer_class = CashTransactionSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        return CashTransaction.objects.filter(perfil=self.request.user.perfil_prestador)

    def perform_create(self, serializer):
        # La lógica de creación real iría en un servicio para crear también el asiento contable.
        serializer.save(perfil=self.request.user.perfil_prestador)
