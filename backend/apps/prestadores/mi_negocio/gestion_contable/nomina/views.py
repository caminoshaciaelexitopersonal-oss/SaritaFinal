from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction
from decimal import Decimal

from .models import Empleado, Contrato, Planilla, ConceptoNomina, DetalleLiquidacion
from .serializers import EmpleadoSerializer, ContratoSerializer, PlanillaSerializer
from .services import CalculoNominaService
from ..services.nomina import ContabilidadNominaService
from ..services.pagos import ContabilidadPagoService
from ...gestion_financiera.services import PagoService
from ...gestion_financiera.models import CuentaBancaria

class IsPrestadorOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'perfil'):
            return obj.perfil == request.user.perfil_prestador
        if hasattr(obj, 'empleado') and hasattr(obj.empleado, 'perfil'):
            return obj.empleado.perfil == request.user.perfil_prestador
        # Para PlanillaViewSet, el queryset ya está filtrado
        return True

class PlanillaViewSet(viewsets.ModelViewSet):
    serializer_class = PlanillaSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]
    def get_queryset(self):
        return Planilla.objects.filter(perfil=self.request.user.perfil_prestador)

    @action(detail=True, methods=['post'], url_path='liquidar')
    @transaction.atomic
    def liquidar_planilla(self, request, pk=None):
        # ... (lógica de liquidación)
        pass

    @action(detail=True, methods=['post'], url_path='pagar')
    @transaction.atomic
    def pagar_planilla(self, request, pk=None):
        planilla = self.get_object()
        perfil = request.user.perfil_prestador
        cuenta_bancaria_id = request.data.get('cuenta_bancaria_id')

        if planilla.estado != Planilla.EstadoPlanilla.CONTABILIZADA:
            return Response({"error": "La planilla debe estar contabilizada."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            cuenta_bancaria = CuentaBancaria.objects.get(id=cuenta_bancaria_id, perfil=perfil)
        except CuentaBancaria.DoesNotExist:
            return Response({"error": "Cuenta bancaria no encontrada."}, status=status.HTTP_404_NOT_FOUND)

        for detalle in planilla.detalles_liquidacion.all():
            orden_pago = PagoService.crear_orden_pago_empleado(
                perfil=perfil,
                cuenta_bancaria=cuenta_bancaria,
                empleado=detalle.empleado,
                monto=detalle.salario_base, # Simplificación
                concepto=f"Pago nómina {planilla.periodo_inicio}"
            )
            ContabilidadPagoService.contabilizar_pago(orden_pago)

        planilla.estado = Planilla.EstadoPlanilla.PAGADA
        planilla.save()
        return Response({"status": "Nómina pagada."})
