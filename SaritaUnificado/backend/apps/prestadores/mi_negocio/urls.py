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
from .gestion_operativa.modulos_especializados.views.hoteles import (
    HabitacionViewSet,
    ServicioAdicionalHotelViewSet
)
from .gestion_operativa.modulos_especializados.views.restaurantes import (
    CategoriaMenuViewSet,
    ProductoMenuViewSet,
    MesaViewSet,
    ReservaMesaViewSet
)
from .gestion_operativa.modulos_especializados.views.guias import (
    RutaViewSet,
    HitoRutaViewSet,
    EquipamientoViewSet
)
from .gestion_operativa.modulos_especializados.views.transporte import (
    VehiculoViewSet,
    ConductorViewSet
)
from .gestion_operativa.modulos_especializados.views.agencias import (
    PaqueteTuristicoViewSet,
    ItinerarioViewSet
)
from .gestion_operativa.modulos_especializados.views.artesanos import (
    CategoriaProductoArtesanalViewSet,
    ProductoArtesanalViewSet,
    PedidoViewSet
)

router = routers.DefaultRouter()
# Módulos Genéricos
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

# Módulos Especializados
# Hoteles
router.register(r'hoteles/habitaciones', HabitacionViewSet, basename='habitaciones')
router.register(r'hoteles/servicios-adicionales', ServicioAdicionalHotelViewSet, basename='servicios-adicionales-hotel')
# Restaurantes
router.register(r'restaurantes/menu/categorias', CategoriaMenuViewSet, basename='menu-categorias')
router.register(r'restaurantes/menu/productos', ProductoMenuViewSet, basename='menu-productos')
router.register(r'restaurantes/mesas', MesaViewSet, basename='mesas')
router.register(r'restaurantes/reservas-mesas', ReservaMesaViewSet, basename='reservas-mesas')
# Guías Turísticos
router.register(r'guias/rutas', RutaViewSet, basename='rutas')
router.register(r'guias/rutas-hitos', HitoRutaViewSet, basename='rutas-hitos')
router.register(r'guias/equipamiento', EquipamientoViewSet, basename='equipamiento')
# Transporte Turístico
router.register(r'transporte/vehiculos', VehiculoViewSet, basename='vehiculos')
router.register(r'transporte/conductores', ConductorViewSet, basename='conductores')
# Agencias de Viajes
router.register(r'agencias/paquetes', PaqueteTuristicoViewSet, basename='paquetes')
router.register(r'agencias/itinerarios', ItinerarioViewSet, basename='itinerarios')
# Artesanos
router.register(r'artesanos/productos', ProductoArtesanalViewSet, basename='productos-artesanales')
router.register(r'artesanos/categorias', CategoriaProductoArtesanalViewSet, basename='categorias-artesanales')
router.register(r'artesanos/pedidos', PedidoViewSet, basename='pedidos-artesanales')


urlpatterns = router.urls
