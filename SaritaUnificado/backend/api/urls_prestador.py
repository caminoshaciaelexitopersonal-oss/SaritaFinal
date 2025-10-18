from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views as api_views
from empresa import views as empresa_views
from turismo import views as turismo_views
from restaurante import views as restaurante_views

# Router para el panel de prestadores
router = DefaultRouter()

# --- Gestión Operativa (ViewSets) ---
router.register(r'mi-negocio/operativa/productos', empresa_views.ProductoViewSet, basename='mi-negocio-productos')
router.register(r'mi-negocio/operativa/clientes', empresa_views.ClienteViewSet, basename='mi-negocio-clientes')
router.register(r'mi-negocio/operativa/documentos', api_views.DocumentoVerificacionViewSet, basename='mi-negocio-documentos')
router.register(r'mi-negocio/operativa/valoraciones', api_views.PrestadorResenaViewSet, basename='mi-negocio-valoraciones')
router.register(r'mi-negocio/operativa/reservas', turismo_views.ReservaViewSet, basename='mi-negocio-reservas')
router.register(r'mi-negocio/operativa/inventario', empresa_views.InventarioViewSet, basename='mi-negocio-inventario')
router.register(r'mi-negocio/operativa/costos', empresa_views.CostoViewSet, basename='mi-negocio-costos')
router.register(r'mi-negocio/operativa/hoteles/habitaciones', turismo_views.HabitacionViewSet, basename='mi-negocio-hotel-habitaciones')
router.register(r'mi-negocio/operativa/restaurantes/menu', restaurante_views.CategoriaConProductosViewSet, basename='mi-negocio-restaurante-menu')
router.register(r'mi-negocio/operativa/restaurantes/mesas', restaurante_views.MesaViewSet, basename='mi-negocio-restaurante-mesas')
router.register(r'mi-negocio/operativa/guias/rutas', turismo_views.RutaTuristicaViewSet, basename='mi-negocio-guia-rutas')
# Los siguientes ViewSets están comentados en turismo/views.py porque los modelos no existen.
# router.register(r'mi-negocio/operativa/transporte/vehiculos', turismo_views.VehiculoTuristicoViewSet, basename='mi-negocio-transporte-vehiculos')
# router.register(r'mi-negocio/operativa/agencias/paquetes', turismo_views.PaqueteTuristicoViewSet, basename='mi-negocio-agencia-paquetes')


# --- Vistas Individuales (no son ViewSets) ---
urlpatterns = [
    path('mi-negocio/operativa/perfil/', api_views.PrestadorProfileView.as_view(), name='mi-negocio-perfil'),
    path('mi-negocio/operativa/galeria/', api_views.ImagenGaleriaView.as_view(), name='mi-negocio-galeria'),
    path('mi-negocio/operativa/estadisticas/', api_views.PrestadorDashboardAnalyticsView.as_view(), name='mi-negocio-estadisticas'),
    # Incluir las rutas generadas por el router
    path('', include(router.urls)),
]