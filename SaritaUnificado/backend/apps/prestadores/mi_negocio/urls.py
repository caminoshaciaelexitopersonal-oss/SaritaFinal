from django.urls import path, include
from rest_framework_nested import routers
from .gestion_operativa.modulos_genericos.perfil.views import PerfilViewSet
from .gestion_operativa.modulos_genericos.productos_servicios.views import ProductoServicioViewSet
from .gestion_operativa.modulos_genericos.crm.views import ClienteViewSet
from .gestion_operativa.modulos_genericos.costos.views import CostoViewSet
from .gestion_operativa.modulos_genericos.inventario.views import InventarioViewSet
from .gestion_operativa.modulos_genericos.reservas.views import ReservaViewSet
from .gestion_operativa.modulos_genericos.rat.views import RegistroActividadTuristicaViewSet
from .gestion_operativa.modulos_genericos.soporte.views import TicketSoporteViewSet
from .gestion_operativa.modulos_genericos.views.configuracion import ConfiguracionPrestadorViewSet
from .gestion_operativa.modulos_genericos.views.reportes import ReporteViewSet
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
