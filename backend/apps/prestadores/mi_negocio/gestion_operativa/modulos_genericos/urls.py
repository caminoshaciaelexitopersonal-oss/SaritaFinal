# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .perfil.views import PerfilViewSet
from .clientes.views import ClienteViewSet
from .productos_servicios.views import ProductViewSet
from .inventario.views import InventoryItemViewSet
from .costos.views import CostoViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet, basename='cliente')
router.register(r'productos-servicios', ProductViewSet, basename='producto-servicio')
router.register(r'inventario', InventoryItemViewSet, basename='inventario')
router.register(r'costos', CostoViewSet, basename='costo')

# El PerfilViewSet no usa un router estándar porque tiene acciones personalizadas
perfil_urls = [
    path('perfil/me/', PerfilViewSet.as_view({'get': 'me'}), name='perfil-me'),
    path('perfil/update-me/', PerfilViewSet.as_view({'put': 'update_me', 'patch': 'update_me'}), name='perfil-update-me'),
]

urlpatterns = [
    path('', include(router.urls)),
    path('', include(perfil_urls)),
    # Módulos especializados
    path('hotel/', include('apps.prestadores.mi_negocio.gestion_operativa.modulos_especializados.hoteles.urls')),
    path('restaurante/', include('apps.prestadores.mi_negocio.gestion_operativa.modulos_especializados.restaurantes.urls')),
    path('guias/', include('apps.prestadores.mi_negocio.gestion_operativa.modulos_especializados.guias.urls')),
    path('transporte/', include('apps.prestadores.mi_negocio.gestion_operativa.modulos_especializados.transporte.urls')),
    path('agencias-viajes/', include('apps.prestadores.mi_negocio.gestion_operativa.modulos_especializados.agencias_de_viajes.urls')),
    path('arrendadora-vehiculos/', include('apps.prestadores.mi_negocio.gestion_operativa.modulos_especializados.arrendadoras_vehiculos.urls')),
    path('sitios-turisticos/', include('apps.prestadores.mi_negocio.gestion_operativa.modulos_especializados.sitios_turisticos.urls')),
]
