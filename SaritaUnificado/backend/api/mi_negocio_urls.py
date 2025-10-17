from django.urls import path, include
from rest_framework.routers import DefaultRouter
from empresa.views import ProductoViewSet, RegistroClienteViewSet
from turismo.views import (
    HotelViewSet,
    HabitacionViewSet,
    ReservaTuristicaViewSet,
    GuiaTuristicoViewSet,
    VehiculoTuristicoViewSet,
    PaqueteTuristicoViewSet
)
from restaurante.views import (
    CategoriaMenuViewSet,
    ProductoMenuViewSet,
    MesaViewSet,
    PedidoViewSet
)

router = DefaultRouter()

# Módulos de Empresa (Genéricos)
router.register(r'productos', ProductoViewSet, basename='negocio-producto')
router.register(r'clientes', RegistroClienteViewSet, basename='negocio-cliente')

# Módulos de Turismo
router.register(r'hoteles', HotelViewSet, basename='negocio-hotel')
router.register(r'habitaciones', HabitacionViewSet, basename='negocio-habitacion')
router.register(r'reservas', ReservaTuristicaViewSet, basename='negocio-reserva')
router.register(r'guias', GuiaTuristicoViewSet, basename='negocio-guia')
router.register(r'vehiculos', VehiculoTuristicoViewSet, basename='negocio-vehiculo')
router.register(r'paquetes', PaqueteTuristicoViewSet, basename='negocio-paquete')

# Módulos de Restaurante
router.register(r'menu-categorias', CategoriaMenuViewSet, basename='negocio-menu-categoria')
router.register(r'menu-productos', ProductoMenuViewSet, basename='negocio-menu-producto')
router.register(r'mesas', MesaViewSet, basename='negocio-mesa')
router.register(r'pedidos', PedidoViewSet, basename='negocio-pedido')

urlpatterns = [
    path('', include(router.urls)),
]