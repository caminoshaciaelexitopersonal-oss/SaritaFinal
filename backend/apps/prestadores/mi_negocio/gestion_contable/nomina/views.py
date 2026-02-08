from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Empleado, Contrato, Planilla, ConceptoNomina, DetalleLiquidacion
from .serializers import *
from .sargentos import SargentoNomina

class IsPrestadorOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.perfil == request.user.perfil_prestador

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

    @action(detail=True, methods=['post'])
    def liquidar(self, request, pk=None):
        planilla = self.get_object()
        empleados = Empleado.objects.filter(perfil=request.user.perfil_prestador)
        for emp in empleados:
            SargentoNomina.liquidar_empleado(planilla.id, emp.id, request.user.id)

        planilla.estado = Planilla.EstadoPlanilla.LIQUIDADA
        planilla.save()
        return Response({"status": "Planilla liquidada exitosamente."})

    @action(detail=True, methods=['post'])
    def contabilizar(self, request, pk=None):
        try:
            resultado = SargentoNomina.contabilizar_y_pagar(pk, request.user.id)
            return Response(resultado)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ConceptoNominaViewSet(viewsets.ModelViewSet):
    queryset = ConceptoNomina.objects.all()
    serializer_class = ConceptoNominaSerializer
    permission_classes = [permissions.IsAuthenticated]
