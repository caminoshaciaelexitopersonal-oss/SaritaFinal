# backend/apps/financiera/views.py
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .models import BankAccount, CashTransaction
from .serializers import BankAccountSerializer, CashTransactionSerializer

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Para CashTransaction, el perfil está en la cuenta bancaria.
        if hasattr(obj, 'bank_account'):
            return obj.bank_account.perfil == request.user.perfil_prestador
        return obj.perfil == request.user.perfil_prestador

class BankAccountViewSet(viewsets.ModelViewSet):
    serializer_class = BankAccountSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'perfil_prestador'):
            return BankAccount.objects.filter(perfil=user.perfil_prestador)
        return BankAccount.objects.none()

    def perform_create(self, serializer):
        serializer.save(perfil=self.request.user.perfil_prestador)

class CashTransactionViewSet(viewsets.ModelViewSet):
    serializer_class = CashTransactionSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'perfil_prestador'):
            return CashTransaction.objects.filter(bank_account__perfil=user.perfil_prestador)
        return CashTransaction.objects.none()

    def perform_create(self, serializer):
        # Asignar el perfil basado en la cuenta bancaria para consistencia
        bank_account = serializer.validated_data['bank_account']
        serializer.save(
            perfil=bank_account.perfil,
            created_by=self.request.user
        )
