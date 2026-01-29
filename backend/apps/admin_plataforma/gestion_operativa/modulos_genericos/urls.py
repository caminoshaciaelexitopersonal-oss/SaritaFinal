from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .perfil.views import PerfilViewSet
from .clientes.views import ClienteViewSet
from .productos_servicios.views import ProductViewSet
from .inventario.views import InventoryItemViewSet
from .costos.views import CostoViewSet
from .horarios.views import HorarioViewSet, ExcepcionHorarioViewSet
from .reservas.views import ReservaViewSet, PoliticaCancelacionViewSet
from .valoraciones.views import ValoracionViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet, basename='cliente')
router.register(r'productos-servicios', ProductViewSet, basename='producto-servicio')
router.register(r'inventario', InventoryItemViewSet, basename='inventario')
router.register(r'costos', CostoViewSet, basename='costo')
router.register(r'horarios', HorarioViewSet, basename='horario')
router.register(r'horarios-excepciones', ExcepcionHorarioViewSet, basename='horario-excepcion')
router.register(r'reservas', ReservaViewSet, basename='reserva')
router.register(r'politicas-cancelacion', PoliticaCancelacionViewSet, basename='politica-cancelacion')
router.register(r'valoraciones', ValoracionViewSet, basename='valoracion')

perfil_urls = [
    path('perfil/me/', PerfilViewSet.as_view({'get': 'me'}), name='perfil-me'),
    path('perfil/update-me/', PerfilViewSet.as_view({'put': 'update_me', 'patch': 'update_me'}), name='perfil-update-me'),
]

urlpatterns = [
    path('', include(router.urls)),
    path('', include(perfil_urls)),

    # Módulos especializados
    path('hotel/', include('apps.admin_plataforma.gestion_operativa.modulos_especializados.hoteles.urls')),
    path('restaurante/', include('apps.admin_plataforma.gestion_operativa.modulos_especializados.restaurantes.urls')),
    path('guias/', include('apps.admin_plataforma.gestion_operativa.modulos_especializados.guias.urls')),
    path('transporte/', include('apps.admin_plataforma.gestion_operativa.modulos_especializados.transporte.urls')),
]
