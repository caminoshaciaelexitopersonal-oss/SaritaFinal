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

router = routers.DefaultRouter()
router.register(r'perfil', PerfilViewSet, basename='perfil')
router.register(r'productos', ProductoServicioViewSet, basename='productos')
router.register(r'clientes', ClienteViewSet, basename='clientes')
router.register(r'costos', CostoViewSet, basename='costos')
router.register(r'inventario', InventarioViewSet, basename='inventario')
router.register(r'reservas', ReservaViewSet, basename='reservas')
router.register(r'rat', RegistroActividadTuristicaViewSet, basename='rat')
router.register(r'reportes', ReporteViewSet, basename='reportes')
router.register(r'soporte', TicketSoporteViewSet, basename='soporte')
router.register(r'configuracion', ConfiguracionPrestadorViewSet, basename='configuracion')

urlpatterns = router.urls
