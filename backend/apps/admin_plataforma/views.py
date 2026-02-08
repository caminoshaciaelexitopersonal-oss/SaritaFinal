
from rest_framework import viewsets, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from drf_spectacular.utils import extend_schema
from .services.gestion_plataforma_service import GestionPlataformaService
from .services.governance_kernel import GovernanceKernel
from .models import Plan, Suscripcion
from .serializers import PlanSerializer, SuscripcionSerializer
from apps.admin_plataforma.gestion_operativa.modulos_genericos.perfil.serializers import PerfilSerializer
from apps.admin_plataforma.mixins import SystemicERPViewSetMixin
from api.permissions import IsSuperAdmin

class MetaStandardView(APIView):
    """
    Vista para obtener la doctrina de la FASE META (Estándar SARITA).
    """
    permission_classes = [IsAdminUser]

    @extend_schema(responses={200: serializers.JSONField()})
    def get(self, request):
        kernel = GovernanceKernel(user=request.user)
        metadata = kernel.get_meta_standard_metadata()
        return Response(metadata)

class SaritaProfileView(APIView):
    """
    Vista para obtener el perfil empresarial de la Plataforma Sarita.
    """
    permission_classes = [IsAdminUser]
    serializer_class = PerfilSerializer

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
        result = kernel.resolve_and_execute(
            intention_name="PLATFORM_CREATE_PLAN",
            parameters=serializer.validated_data
        )
        # Asignar la instancia creada al serializer para que la respuesta sea correcta
        serializer.instance = result.get("instance")

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
