# backend/apps/financiera/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import BankAccount, CashTransaction
from .serializers import BankAccountSerializer, CashTransactionSerializer
from api.permissions import IsOwnerOrReadOnly

class BankAccountViewSet(viewsets.ModelViewSet):
    serializer_class = BankAccountSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'perfil_prestador'):
            return BankAccount.objects.filter(perfil=user.perfil_prestador).order_by('bank_name')
        return BankAccount.objects.none()

    def perform_create(self, serializer):
        serializer.save(perfil=self.request.user.perfil_prestador)

class CashTransactionViewSet(viewsets.ModelViewSet):
    serializer_class = CashTransactionSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'perfil_prestador'):
            return CashTransaction.objects.filter(bank_account__perfil=user.perfil_prestador).order_by('-date')
        return CashTransaction.objects.none()

    def perform_create(self, serializer):
        """
        Asigna el perfil y el creador a la transacción.
        El perfil se deriva de la cuenta bancaria para asegurar la consistencia.
        """
        bank_account = serializer.validated_data['bank_account']
        serializer.save(
            perfil=self.request.user.perfil_prestador,
            created_by=self.request.user
        )
