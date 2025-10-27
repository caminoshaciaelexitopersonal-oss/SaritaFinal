# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .perfil.views import PerfilViewSet
from .clientes.views import ClienteViewSet
from .productos_servicios.views import ProductoServicioViewSet
from .inventario.views import InventarioViewSet
from .costos.views import CostoViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet, basename='cliente')
router.register(r'productos-servicios', ProductoServicioViewSet, basename='producto-servicio')
router.register(r'inventario', InventarioViewSet, basename='inventario')
router.register(r'costos', CostoViewSet, basename='costo')

# El PerfilViewSet no usa un router estándar porque tiene acciones personalizadas
perfil_urls = [
    path('perfil/me/', PerfilViewSet.as_view({'get': 'me'}), name='perfil-me'),
    path('perfil/update-me/', PerfilViewSet.as_view({'put': 'update_me', 'patch': 'update_me'}), name='perfil-update-me'),
]

urlpatterns = [
    path('', include(router.urls)),
    path('', include(perfil_urls)),
]
