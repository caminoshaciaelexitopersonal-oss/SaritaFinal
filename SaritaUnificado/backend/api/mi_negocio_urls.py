from django.urls import path, include
from rest_framework_nested import routers
from empresa.views import ClienteViewSet, ProductoViewSet
from turismo.views import (
    HotelViewSet, HabitacionViewSet, TarifaViewSet, DisponibilidadViewSet,
    ReservaViewSet, RutaTuristicaViewSet, VehiculoTuristicoViewSet, PaqueteTuristicoViewSet
)
from .views import PrestadorProfileView, PrestadorResenaViewSet, ImagenGaleriaView, ImagenGaleriaDetailView

# --- Router Principal para "Mi Negocio" ---
router = routers.DefaultRouter()

# --- Gestión Operativa ---
# Módulos Genéricos
router.register(r'productos', ProductoViewSet, basename='negocio-productos')
router.register(r'clientes', ClienteViewSet, basename='negocio-clientes')
router.register(r'reservas', ReservaViewSet, basename='negocio-reservas')
router.register(r'tarifas', TarifaViewSet, basename='negocio-tarifas')
router.register(r'disponibilidades', DisponibilidadViewSet, basename='negocio-disponibilidades')

# Módulos Especializados
router.register(r'hoteles', HotelViewSet, basename='negocio-hoteles')
router.register(r'rutas', RutaTuristicaViewSet, basename='negocio-rutas')
router.register(r'vehiculos', VehiculoTuristicoViewSet, basename='negocio-vehiculos')
router.register(r'paquetes', PaqueteTuristicoViewSet, basename='negocio-paquetes')

# --- Rutas Anidadas ---
# /hoteles/{hotel_pk}/habitaciones/
habitaciones_router = routers.NestedSimpleRouter(router, r'hoteles', lookup='hotel')
habitaciones_router.register(r'habitaciones', HabitacionViewSet, basename='hotel-habitaciones')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(habitaciones_router.urls)),

    # Endpoints que no son ViewSets (perfil, valoraciones, etc.)
    path('perfil/', PrestadorProfileView.as_view(), name='negocio-perfil'),
    path('valoraciones/', PrestadorResenaViewSet.as_view({'get': 'list'}), name='negocio-valoraciones'),
    path('galeria/', ImagenGaleriaView.as_view(), name='negocio-galeria'),
    path('galeria/<int:pk>/', ImagenGaleriaDetailView.as_view(), name='negocio-galeria-detail'),
]