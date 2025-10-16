from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'hoteles', views.HotelViewSet, basename='hotel')
router.register(r'habitaciones', views.HabitacionViewSet, basename='habitacion')
router.register(r'guias', views.GuiaTuristicoViewSet, basename='guia')
router.register(r'vehiculos', views.VehiculoTuristicoViewSet, basename='vehiculo')
router.register(r'paquetes', views.PaqueteTuristicoViewSet, basename='paquete')
router.register(r'reservas', views.ReservaViewSet, basename='reserva')

urlpatterns = [
    path('', include(router.urls)),
]