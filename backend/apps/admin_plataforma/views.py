
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .services.gestion_plataforma_service import GestionPlataformaService
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.perfil.serializers import PerfilSerializer

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
