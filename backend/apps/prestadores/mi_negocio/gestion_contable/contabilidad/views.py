# backend/apps/prestadores/mi_negocio/gestion_contable/views.py
from rest_framework import viewsets, permissions
from .models import (
    PlanDeCuentas,
    Cuenta,
    PeriodoContable,
    AsientoContable,
)
from .serializers import (
    PlanDeCuentasSerializer,
    CuentaSerializer,
    PeriodoContableSerializer,
    AsientoContableSerializer,
)

class BaseTenantViewSet(viewsets.ModelViewSet):
    """
    ViewSet base que filtra automáticamente los objetos
    por el 'provider' (inquilino) del usuario autenticado.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Asegurarse de que el usuario tenga un perfil de prestador
        if hasattr(self.request.user, 'perfil_prestador'):
            provider = self.request.user.perfil_prestador
            return self.queryset.filter(provider=provider)
        # Si no tiene perfil, no debería ver ningún dato.
        return self.queryset.none()

    def perform_create(self, serializer):
        # Asigna automáticamente el 'provider' al crear un objeto.
        if hasattr(self.request.user, 'perfil_prestador'):
            serializer.save(provider=self.request.user.perfil_prestador)
        else:
            # Opcional: Lanzar un error si se intenta crear sin perfil
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("No tienes un perfil de prestador para crear este objeto.")


class PlanDeCuentasViewSet(BaseTenantViewSet):
    """
    API endpoint para el Plan de Cuentas.
    """
    queryset = PlanDeCuentas.objects.all().prefetch_related('cuentas')
    serializer_class = PlanDeCuentasSerializer


class CuentaViewSet(BaseTenantViewSet):
    """
    API endpoint para las Cuentas Contables.
    """
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer
    filterset_fields = ['plan_de_cuentas', 'tipo', 'parent']


class PeriodoContableViewSet(BaseTenantViewSet):
    """
    API endpoint para los Períodos Contables.
    """
    queryset = PeriodoContable.objects.all()
    serializer_class = PeriodoContableSerializer
    filterset_fields = ['cerrado']


from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import (
    PlanDeCuentas,
    Cuenta,
    PeriodoContable,
    AsientoContable,
)
from .serializers import (
    PlanDeCuentasSerializer,
    CuentaSerializer,
    PeriodoContableSerializer,
    AsientoContableSerializer,
    TransaccionSerializer,
)
from .services import ContabilidadService, ContabilidadValidationError


class AsientoContableViewSet(BaseTenantViewSet):
    """
    API endpoint para los Asientos Contables.
    La creación se gestiona a través del ContabilidadService para asegurar la integridad.
    """
    queryset = AsientoContable.objects.all().prefetch_related('transacciones')
    serializer_class = AsientoContableSerializer
    filterset_fields = ['periodo', 'fecha']

    @action(detail=False, methods=['get'])
    def libro_diario(self, request):
        fecha_inicio = request.query_params.get('fecha_inicio')
        fecha_fin = request.query_params.get('fecha_fin')

        if not fecha_inicio or not fecha_fin:
            return Response({"error": "Debe proporcionar fecha_inicio y fecha_fin"}, status=status.HTTP_400_BAD_REQUEST)

        provider = request.user.perfil_prestador
        asientos = ContabilidadService.obtener_libro_diario(provider, fecha_inicio, fecha_fin)
        serializer = self.get_serializer(asientos, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def balance_comprobacion(self, request):
        periodo_id = request.query_params.get('periodo_id')
        if not periodo_id:
            return Response({"error": "Debe proporcionar periodo_id"}, status=status.HTTP_400_BAD_REQUEST)

        provider = request.user.perfil_prestador
        balance = ContabilidadService.generar_balance_comprobacion(provider, periodo_id)
        return Response(balance)

    @action(detail=False, methods=['get'])
    def estado_resultados(self, request):
        fecha_inicio = request.query_params.get('fecha_inicio')
        fecha_fin = request.query_params.get('fecha_fin')
        if not fecha_inicio or not fecha_fin:
            return Response({"error": "Debe proporcionar fecha_inicio y fecha_fin"}, status=status.HTTP_400_BAD_REQUEST)

        provider = request.user.perfil_prestador
        reporte = ContabilidadService.generar_estado_resultados(provider, fecha_inicio, fecha_fin)
        return Response(reporte)

    @action(detail=False, methods=['get'])
    def balance_general(self, request):
        fecha_corte = request.query_params.get('fecha_corte')
        if not fecha_corte:
            return Response({"error": "Debe proporcionar fecha_corte"}, status=status.HTTP_400_BAD_REQUEST)

        provider = request.user.perfil_prestador
        reporte = ContabilidadService.generar_balance_general(provider, fecha_corte)
        return Response(reporte)

    @action(detail=False, methods=['get'])
    def flujo_caja(self, request):
        fecha_inicio = request.query_params.get('fecha_inicio')
        fecha_fin = request.query_params.get('fecha_fin')
        if not fecha_inicio or not fecha_fin:
            return Response({"error": "Debe proporcionar fecha_inicio y fecha_fin"}, status=status.HTTP_400_BAD_REQUEST)

        provider = request.user.perfil_prestador
        reporte = ContabilidadService.generar_flujo_caja(provider, fecha_inicio, fecha_fin)
        return Response(reporte)

    @action(detail=False, methods=['get'])
    def libro_mayor(self, request):
        cuenta_codigo = request.query_params.get('cuenta_codigo')
        fecha_inicio = request.query_params.get('fecha_inicio')
        fecha_fin = request.query_params.get('fecha_fin')

        if not cuenta_codigo or not fecha_inicio or not fecha_fin:
            return Response({"error": "Faltan parámetros: cuenta_codigo, fecha_inicio, fecha_fin"}, status=status.HTTP_400_BAD_REQUEST)

        provider = request.user.perfil_prestador
        movimientos = ContabilidadService.obtener_libro_mayor(provider, cuenta_codigo, fecha_inicio, fecha_fin)
        serializer = TransaccionSerializer(movimientos, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Extraer los datos validados
        validated_data = serializer.validated_data
        transacciones_data = validated_data.pop('transacciones')

        try:
            if not hasattr(request.user, 'perfil_prestador'):
                 raise ContabilidadValidationError("No tienes un perfil de prestador asignado.")

            # Llamar al servicio para la creación
            asiento = ContabilidadService.crear_asiento_completo(
                provider=request.user.perfil_prestador,
                creado_por=request.user,
                transacciones_data=transacciones_data,
                **validated_data
            )

            # Devolver la representación del asiento creado
            response_serializer = self.get_serializer(asiento)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        except ContabilidadValidationError as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
