from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import transaction

from .models import Empleado, Contrato, Planilla, ConceptoNomina, DetalleLiquidacion
from .serializers import EmpleadoSerializer, ContratoSerializer, PlanillaSerializer, ConceptoNominaSerializer
from .services import CalculoNominaService, ContabilidadNominaService

class IsPrestadorOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'perfil'):
            return obj.perfil == request.user.perfil_prestador
        if hasattr(obj, 'empleado') and hasattr(obj.empleado, 'perfil'):
             return obj.empleado.perfil == request.user.perfil_prestador
        return False

class EmpleadoViewSet(viewsets.ModelViewSet):
    serializer_class = EmpleadoSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        return Empleado.objects.filter(perfil=self.request.user.perfil_prestador)

class ContratoViewSet(viewsets.ModelViewSet):
    serializer_class = ContratoSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        return Contrato.objects.filter(empleado__perfil=self.request.user.perfil_prestador)

class PlanillaViewSet(viewsets.ModelViewSet):
    serializer_class = PlanillaSerializer
    permission_classes = [permissions.IsAuthenticated, IsPrestadorOwner]

    def get_queryset(self):
        return Planilla.objects.filter(perfil=self.request.user.perfil_prestador)

    @action(detail=True, methods=['post'], url_path='liquidar')
    @transaction.atomic
    def liquidar_planilla(self, request, pk=None):
        planilla = self.get_object()

        if planilla.estado != Planilla.EstadoPlanilla.BORRADOR:
            return Response(
                {"error": "La planilla ya ha sido liquidada o está en proceso."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Eliminar liquidaciones anteriores para esta planilla si existen
        DetalleLiquidacion.objects.filter(planilla=planilla).delete()

        empleados_activos = Empleado.objects.filter(perfil=request.user.perfil_prestador, contratos__activo=True)

        for empleado in empleados_activos:
            try:
                contrato_activo = empleado.contratos.get(activo=True)
                service = CalculoNominaService(
                    contrato=contrato_activo,
                    fecha_inicio=planilla.periodo_inicio,
                    fecha_fin=planilla.periodo_fin
                )

                # Realizar cálculos
                valor_cesantias = service.calcular_cesantias()
                parafiscales = service.calcular_parafiscales()

                # Guardar el detalle
                DetalleLiquidacion.objects.create(
                    planilla=planilla,
                    empleado=empleado,
                    salario_base=contrato_activo.salario,
                    dias_trabajados=service.dias_trabajados,
                    valor_prima=service.calcular_prima(),
                    valor_cesantias=valor_cesantias,
                    valor_intereses_cesantias=service.calcular_intereses_cesantias(valor_cesantias),
                    valor_vacaciones=service.calcular_vacaciones(),
                    valor_aporte_ccf=parafiscales['aporte_ccf'],
                    valor_aporte_icbf=parafiscales['aporte_icbf'],
                    valor_aporte_sena=parafiscales['aporte_sena'],
                )
            except Contrato.DoesNotExist:
                # Opcional: manejar empleados sin contrato activo
                continue

        # Contabilizar la liquidación
        try:
            contabilidad_service = ContabilidadNominaService(planilla)
            contabilidad_service.contabilizar_liquidacion()
        except Exception as e:
            # Si falla la contabilidad, la transacción se revierte.
            return Response(
                {"error": f"Error durante la contabilización: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        planilla.estado = Planilla.EstadoPlanilla.CONTABILIZADA
        planilla.save()

        return Response(
            {"status": "Planilla liquidada y contabilizada correctamente."},
            status=status.HTTP_200_OK
        )

class ConceptoNominaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ConceptoNomina.objects.all()
    serializer_class = ConceptoNominaSerializer
    permission_classes = [permissions.IsAuthenticated]
