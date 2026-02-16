# backend/apps/prestadores/mi_negocio/gestion_operativa/modulos_genericos/urls.py
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

urlpatterns = [
    path('', include(router.urls)),
    # Módulos de Operativa Turística (Reestructurados Fase 16)
    path('hotel/', include('apps.prestadores.mi_negocio.operativa_turistica.operadores_directos.hoteles.urls')),
    path('restaurante/', include('apps.prestadores.mi_negocio.operativa_turistica.operadores_directos.restaurantes.urls')),
    path('transporte/', include('apps.prestadores.mi_negocio.operativa_turistica.operadores_directos.transporte.urls')),
    path('guias/', include('apps.prestadores.mi_negocio.operativa_turistica.operadores_directos.guias.urls')),
    path('agencias/', include('apps.prestadores.mi_negocio.operativa_turistica.operadores_directos.agencias.urls')),
    path('eventos/', include('apps.prestadores.mi_negocio.operativa_turistica.operadores_directos.eventos.urls')),
    path('bares-discotecas/', include('apps.prestadores.mi_negocio.operativa_turistica.operadores_directos.bares_discotecas.urls')),
]
