from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import WalletAccount, WalletTransaction
from .serializers import WalletAccountSerializer, WalletTransactionSerializer
from apps.admin_plataforma.services.governance_kernel import GovernanceKernel
from django.db import models

class WalletAccountViewSet(viewsets.ModelViewSet):
    serializer_class = WalletAccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return WalletAccount.objects.all()
        return WalletAccount.objects.filter(user=self.request.user)

    @action(detail=True, methods=['post'])
    def deposit(self, request, pk=None):
        # Permitimos que el turista deposite en su propia cuenta (Vía 3)
        # El Kernel validará el rol.
        kernel = GovernanceKernel(user=request.user)
        try:
            result = kernel.resolve_and_execute(
                intention_name="WALLET_DEPOSIT",
                parameters={
                    "wallet_id": str(pk),
                    "amount": request.data.get("amount"),
                    "description": request.data.get("description", "Carga de fondos institucional")
                }
            )
            return Response(result)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def pay(self, request):
        kernel = GovernanceKernel(user=request.user)
        try:
            result = kernel.resolve_and_execute(
                intention_name="WALLET_PAY",
                parameters={
                    "to_wallet_id": request.data.get("to_wallet_id"),
                    "amount": request.data.get("amount"),
                    "related_service_id": request.data.get("related_service_id"),
                    "description": request.data.get("description")
                }
            )
            return Response(result)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def liquidate(self, request, pk=None):
        kernel = GovernanceKernel(user=request.user)
        try:
            result = kernel.resolve_and_execute(
                intention_name="WALLET_LIQUIDATE",
                parameters={"wallet_id": str(pk)}
            )
            return Response(result)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def freeze(self, request, pk=None):
        kernel = GovernanceKernel(user=request.user)
        try:
            result = kernel.resolve_and_execute(
                intention_name="WALLET_FREEZE",
                parameters={
                    "wallet_id": str(pk),
                    "motivo": request.data.get("motivo")
                }
            )
            return Response(result)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class WalletTransactionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = WalletTransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return WalletTransaction.objects.all()
        # Transacciones donde el usuario es origen o destino
        return WalletTransaction.objects.filter(
            models.Q(from_wallet__user=self.request.user) |
            models.Q(to_wallet__user=self.request.user)
        )

    @action(detail=True, methods=['post'])
    def refund(self, request, pk=None):
        kernel = GovernanceKernel(user=request.user)
        try:
            result = kernel.resolve_and_execute(
                intention_name="WALLET_REFUND",
                parameters={"transaction_id": str(pk)}
            )
            return Response(result)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
