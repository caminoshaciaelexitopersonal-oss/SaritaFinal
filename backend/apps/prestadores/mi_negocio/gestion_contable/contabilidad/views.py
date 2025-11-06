from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date
from decimal import Decimal
from django.db.models import Sum
from .models import CostCenter, ChartOfAccount, JournalEntry, Transaction
from .serializers import CostCenterSerializer, ChartOfAccountSerializer, JournalEntrySerializer, TransactionSerializer

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

class LibroMayorView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        perfil = request.user.perfil_prestador
        codigo_cuenta = request.query_params.get('codigo_cuenta')
        fecha_inicio_str = request.query_params.get('fecha_inicio', '1900-01-01')
        fecha_fin_str = request.query_params.get('fecha_fin', date.today().isoformat())

        if not codigo_cuenta:
            return Response({"error": "El parámetro 'codigo_cuenta' es requerido."}, status=400)

        try:
            cuenta = ChartOfAccount.objects.get(code=codigo_cuenta)
            fecha_inicio = date.fromisoformat(fecha_inicio_str)
            fecha_fin = date.fromisoformat(fecha_fin_str)
        except (ChartOfAccount.DoesNotExist, ValueError):
            return Response({"error": "Cuenta no encontrada o fechas inválidas."}, status=400)

        transacciones = Transaction.objects.filter(
            journal_entry__perfil=perfil,
            account=cuenta,
            journal_entry__entry_date__range=(fecha_inicio, fecha_fin)
        ).order_by('journal_entry__entry_date', 'id')

        serializer = TransactionSerializer(transacciones, many=True)
        return Response(serializer.data)

class BalanceComprobacionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        perfil = request.user.perfil_prestador
        fecha_fin_str = request.query_params.get('fecha_fin', date.today().isoformat())

        try:
            fecha_fin = date.fromisoformat(fecha_fin_str)
        except ValueError:
            return Response({"error": "Fecha inválida."}, status=400)

        reporte = []
        cuentas = ChartOfAccount.objects.filter(allows_transactions=True)

        total_debitos = Decimal('0.00')
        total_creditos = Decimal('0.00')

        for cuenta in cuentas:
            saldo = Transaction.objects.filter(
                journal_entry__perfil=perfil,
                account=cuenta,
                journal_entry__entry_date__lte=fecha_fin
            ).aggregate(
                total_debit=Sum('debit'),
                total_credit=Sum('credit')
            )

            saldo_deudor = (saldo['total_debit'] or 0) - (saldo['total_credit'] or 0)

            saldo_final_debito = 0
            saldo_final_credito = 0

            if cuenta.nature == 'DEBITO':
                if saldo_deudor > 0: saldo_final_debito = saldo_deudor
                else: saldo_final_credito = -saldo_deudor
            else: # CREDITO
                if saldo_deudor < 0: saldo_final_credito = -saldo_deudor
                else: saldo_final_debito = saldo_deudor

            if saldo_final_debito > 0 or saldo_final_credito > 0:
                reporte.append({
                    "codigo": cuenta.code,
                    "nombre": cuenta.name,
                    "debito": saldo_final_debito,
                    "credito": saldo_final_credito,
                })
                total_debitos += saldo_final_debito
                total_creditos += saldo_final_credito

        return Response({
            "detalle": reporte,
            "totales": {
                "debitos": total_debitos,
                "creditos": total_creditos,
            }
        })

class ReportesFinancierosView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        perfil = request.user.perfil_prestador
        reporte_tipo = request.query_params.get('reporte', 'estado_resultados')
        fecha_fin_str = request.query_params.get('fecha_fin', date.today().isoformat())

        try:
            fecha_fin = date.fromisoformat(fecha_fin_str)
        except ValueError:
            return Response({"error": "Fecha inválida."}, status=400)

        # Usamos la lógica del balance de comprobación como base
        cuentas = ChartOfAccount.objects.filter(allows_transactions=True)

        resultados = []
        total = Decimal('0.00')

        codigos_filtro = []
        if reporte_tipo == 'estado_resultados':
            codigos_filtro = ['4', '5', '6'] # Ingresos, Gastos, Costos
        elif reporte_tipo == 'balance_general':
            codigos_filtro = ['1', '2', '3'] # Activo, Pasivo, Patrimonio

        for cuenta in cuentas:
            if not any(cuenta.code.startswith(c) for c in codigos_filtro):
                continue

            saldo_agg = Transaction.objects.filter(
                journal_entry__perfil=perfil,
                account=cuenta,
                journal_entry__entry_date__lte=fecha_fin
            ).aggregate(saldo=Sum('debit') - Sum('credit'))

            saldo_final = saldo_agg['saldo'] or Decimal('0.00')

            if saldo_final != 0:
                resultados.append({
                    "codigo": cuenta.code,
                    "nombre": cuenta.name,
                    "saldo": saldo_final,
                })
                total += saldo_final

        return Response({
            "reporte": reporte_tipo,
            "fecha": fecha_fin,
            "detalle": resultados,
            "total": total,
        })
