# SaritaUnificado/backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.perfil.views import PerfilViewSet
from backend.clientes.views import ClienteViewSet
from backend.productos_servicios.views import ProductViewSet
from backend.inventario.views import InventoryItemViewSet
from backend.costos.views import CostoViewSet
from backend.horarios.views import HorarioViewSet, ExcepcionHorarioViewSet
from backend.reservas.views import ReservaViewSet, PoliticaCancelacionViewSet
from backend.valoraciones.views import ValoracionViewSet

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

urlpatterns = [
    path('', include(router.urls)),
    # Módulos especializados
    path('alojamiento/', include('apps.prestadores.mi_negocio.gestion_operativa.modulos_especializados.alojamientos.urls')),
    path('gastronomia/', include('apps.prestadores.mi_negocio.gestion_operativa.modulos_especializados.gastronomia.urls')),
    path('hotel/', include('apps.prestadores.mi_negocio.gestion_operativa.modulos_especializados.hoteles.urls')),
    path('restaurante/', include('apps.prestadores.mi_negocio.gestion_operativa.modulos_especializados.restaurantes.urls')),
    path('guias/', include('apps.prestadores.mi_negocio.gestion_operativa.modulos_especializados.guias.urls')),
    path('transportes/', include('apps.prestadores.mi_negocio.gestion_operativa.modulos_especializados.transportes.urls')),
    path('operadores-turisticos/', include('apps.prestadores.mi_negocio.gestion_operativa.modulos_especializados.operadores_turisticos.urls')),
    path('eventos-y-marketing/', include('apps.prestadores.mi_negocio.gestion_operativa.modulos_especializados.eventos.urls')),
    path('transporte/', include('apps.prestadores.mi_negocio.gestion_operativa.modulos_especializados.transporte.urls')),
    path('arrendadora-vehiculos/', include('apps.prestadores.mi_negocio.gestion_operativa.modulos_especializados.arrendadoras_vehiculos.urls')),
    path('sitios-turisticos/', include('apps.prestadores.mi_negocio.gestion_operativa.modulos_especializados.sitios_turisticos.urls')),
]
