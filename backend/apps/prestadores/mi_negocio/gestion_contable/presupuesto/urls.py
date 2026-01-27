from rest_framework.routers import DefaultRouter
from backend.views import PresupuestoViewSet, PartidaPresupuestalViewSet, EjecucionPresupuestalViewSet

router = DefaultRouter()
router.register(r'presupuestos', PresupuestoViewSet, basename='presupuesto')
router.register(r'partidas', PartidaPresupuestalViewSet, basename='partida-presupuestal')
router.register(r'ejecuciones', EjecucionPresupuestalViewSet, basename='ejecucion-presupuestal')

urlpatterns = router.urls
