from django.db.models import Sum, Q
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BankAccount, CashTransaction
from apps.prestadores.mi_negocio.gestion_contable.contabilidad.models import Transaction
from .serializers import (
    BankAccountReadSerializer, BankAccountWriteSerializer,
    CashTransactionReadSerializer, CashTransactionWriteSerializer
)
from apps.prestadores.mi_negocio.permissions import IsPrestadorOwner

class BankAccountViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return BankAccountWriteSerializer
        return BankAccountReadSerializer

    def get_queryset(self):
        return BankAccount.objects.filter(perfil=self.request.user.perfil_prestador)

class CashTransactionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated] # Permiso a nivel de objeto se maneja en el serializer/servicio

    def get_serializer_class(self):
        if self.action == 'create':
            return CashTransactionWriteSerializer
        return CashTransactionReadSerializer

    def get_queryset(self):
        # Asegurarse de que solo se listen transacciones de cuentas que pertenecen al perfil del usuario
        return CashTransaction.objects.filter(
            bank_account__perfil=self.request.user.perfil_prestador
        ).select_related('bank_account', 'journal_entry')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        read_serializer = CashTransactionReadSerializer(instance)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED)

class ReporteIngresosGastosView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        perfil = request.user.perfil_prestador
        fecha_inicio = request.query_params.get('fecha_inicio', '2000-01-01')
        fecha_fin = request.query_params.get('fecha_fin', '2999-12-31')

        # Consulta robusta al libro contable
        transactions = Transaction.objects.filter(
            journal_entry__perfil=perfil,
            journal_entry__entry_date__range=[fecha_inicio, fecha_fin]
        )

        total_ingresos = transactions.filter(
            account__code__startswith='4' # Cuentas de Ingresos
        ).aggregate(total=Sum('credit'))['total'] or 0

        total_gastos = transactions.filter(
            Q(account__code__startswith='5') | Q(account__code__startswith='6') # Cuentas de Gasto y Costo
        ).aggregate(total=Sum('debit'))['total'] or 0

        data = {
            'total_ingresos': total_ingresos,
            'total_gastos': total_gastos,
            'neto': total_ingresos - total_gastos
        }
        return Response(data)
