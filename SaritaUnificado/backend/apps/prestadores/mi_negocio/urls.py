from django.urls import path, include
from rest_framework_nested import routers
from .gestion_operativa.modulos_genericos.views import (
    PerfilViewSet,
    ProductoServicioViewSet,
    ClienteViewSet,
    CostoViewSet,
    InventarioViewSet,
    ReservaViewSet,
    RegistroActividadTuristicaViewSet,
    ReporteViewSet,
    TicketSoporteViewSet,
    ConfiguracionPrestadorViewSet,
)
# ... (el resto de las importaciones de vistas especializadas)

router = routers.DefaultRouter()

# Módulos Genéricos (excluyendo Perfil)
router.register(r'operativa/productos', ProductoServicioViewSet, basename='productos')
router.register(r'operativa/clientes', ClienteViewSet, basename='clientes')
router.register(r'operativa/costos', CostoViewSet, basename='costos')
router.register(r'operativa/inventario', InventarioViewSet, basename='inventario')
router.register(r'operativa/reservas', ReservaViewSet, basename='reservas')
router.register(r'operativa/rat', RegistroActividadTuristicaViewSet, basename='rat')
router.register(r'operativa/reportes', ReporteViewSet, basename='reportes')
router.register(r'operativa/soporte', TicketSoporteViewSet, basename='soporte')
router.register(r'operativa/configuracion', ConfiguracionPrestadorViewSet, basename='configuracion')

# ... (el resto del registro de rutas especializadas)

# Rutas singleton para el Perfil
perfil_urls = [
    path('operativa/perfil/', PerfilViewSet.as_view({'get': 'me', 'put': 'update_me', 'patch': 'update_me'}), name='perfil-me'),
]

urlpatterns = [
    path('', include(router.urls)),
] + perfil_urls
