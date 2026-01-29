
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .services.gestion_plataforma_service import GestionPlataformaService
from .services.governance_kernel import GovernanceKernel
from .models import Plan, Suscripcion
from .serializers import PlanSerializer, SuscripcionSerializer
from apps.admin_plataforma.gestion_operativa.modulos_genericos.perfil.serializers import PerfilSerializer
from apps.admin_plataforma.mixins import SystemicERPViewSetMixin
from api.permissions import IsSuperAdmin

class SaritaProfileView(APIView):
    """
    Vista para obtener el perfil empresarial de la Plataforma Sarita.
    """
    permission_classes = [IsAdminUser]

    def get(self, request):
        """
        Devuelve los detalles del perfil de la plataforma Sarita.
        """
        service = GestionPlataformaService(admin_user=request.user)
        sarita_profile = service.get_sarita_profile()
        serializer = PerfilSerializer(sarita_profile)
        return Response(serializer.data)

class PlanViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    """
    ViewSet para la gestión de Planes de suscripción por parte de los administradores.
    """
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        # Delegar toda decisión al núcleo de orquestación
        kernel = GovernanceKernel(user=self.request.user)
        kernel.resolve_and_execute(
            intention_name="PLATFORM_CREATE_PLAN",
            parameters=serializer.validated_data
        )

class SuscripcionViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    """
    ViewSet para la gestión de Suscripciones de clientes a planes.
    """
    queryset = Suscripcion.objects.all()
    serializer_class = SuscripcionSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        plan = serializer.validated_data['plan']
        cliente = serializer.validated_data['cliente']
        fecha_inicio = serializer.validated_data['fecha_inicio']

        service = GestionPlataformaService(admin_user=self.request.user)
        service.asignar_suscripcion(cliente_profile=cliente, plan=plan, fecha_inicio=fecha_inicio)
