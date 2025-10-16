from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'hoteles', views.HotelViewSet, basename='hotel')
router.register(r'habitaciones', views.HabitacionViewSet, basename='habitacion')
router.register(r'tarifas', views.TarifaViewSet, basename='tarifa')
router.register(r'disponibilidades', views.DisponibilidadViewSet, basename='disponibilidad')
router.register(r'reservas', views.ReservaViewSet, basename='reserva')
router.register(r'rutas-turisticas', views.RutaTuristicaViewSet, basename='ruta-turistica-gestion')

urlpatterns = [
    path('', include(router.urls)),
    path('hoteles/<int:hotel_id>/habitaciones/', views.PublicHabitacionListView.as_view(), name='public-habitaciones-list'),
]