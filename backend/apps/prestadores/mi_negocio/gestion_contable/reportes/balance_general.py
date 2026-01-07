from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.db.models import Sum, Q, F
from decimal import Decimal

from ..cierres.models import PeriodoContable
from apps.prestadores.mi_negocio.gestion_contable.contabilidad.models import ChartOfAccount, Transaction

class BalanceGeneralView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        periodo_id = request.query_params.get('periodo_id')
        if not periodo_id:
            return Response({"error": "Se requiere 'periodo_id'."}, status=400)

        try:
            periodo = PeriodoContable.objects.get(id=periodo_id, perfil=request.user.perfil_prestador)
        except PeriodoContable.DoesNotExist:
            return Response({"error": "Período no encontrado."}, status=404)

        if periodo.estado != PeriodoContable.Estado.CERRADO:
            return Response({"error": "El período debe estar cerrado para generar el reporte."}, status=400)

        # Calcular saldos de cuentas
        saldos = Transaction.objects.filter(
            journal_entry__perfil=request.user.perfil_prestador,
            journal_entry__entry_date__lte=periodo.fecha_fin
        ).values('account__code', 'account__name', 'account__nature').annotate(
            total_debit=Sum('debit'),
            total_credit=Sum('credit')
        ).order_by('account__code')

        activos = []
        pasivos = []
        patrimonio = []
        total_activos = Decimal('0.00')
        total_pasivos_patrimonio = Decimal('0.00')

        for saldo in saldos:
            saldo_final = (saldo['total_debit'] or 0) - (saldo['total_credit'] or 0)

            cuenta = {
                "code": saldo['account__code'],
                "name": saldo['account__name'],
                "balance": saldo_final
            }

            if saldo['account__code'].startswith('1'): # Activos
                activos.append(cuenta)
                total_activos += saldo_final
            elif saldo['account__code'].startswith('2'): # Pasivos
                pasivos.append(cuenta)
                total_pasivos_patrimonio += -saldo_final # Pasivos y Patrimonio son de naturaleza crédito
            elif saldo['account__code'].startswith('3'): # Patrimonio
                patrimonio.append(cuenta)
                total_pasivos_patrimonio += -saldo_final

        return Response({
            "periodo": periodo.nombre,
            "activos": {"items": activos, "total": total_activos},
            "pasivos": {"items": pasivos, "total": sum(c['balance'] for c in pasivos)},
            "patrimonio": {"items": patrimonio, "total": sum(c['balance'] for c in patrimonio)},
            "total_pasivos_y_patrimonio": total_pasivos_patrimonio,
            "verificacion_ecuacion": total_activos == total_pasivos_patrimonio
        })
