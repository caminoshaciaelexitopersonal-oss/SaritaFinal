from rest_framework import viewsets, permissions
from api.permissions import IsSuperAdmin
from apps.admin_plataforma.mixins import SystemicERPViewSetMixin
from apps.prestadores.mi_negocio.gestion_operativa.modulos_genericos.productos_servicios.models import Product
from .serializers import ProductSerializer

class ProductViewSet(SystemicERPViewSetMixin, viewsets.ModelViewSet):
    """
    ViewSet para que el Super Admin gestione los productos/servicios sistémicos.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def perform_create(self, serializer):
        from apps.admin_plataforma.services.gestion_plataforma_service import GestionPlataformaService
        perfil_gobierno = GestionPlataformaService.get_perfil_gobierno()
        serializer.save(provider=perfil_gobierno)
