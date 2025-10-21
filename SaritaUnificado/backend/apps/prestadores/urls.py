from rest_framework.routers import DefaultRouter
from .views import AdminPrestadorViewSet

router = DefaultRouter()
router.register(r'admin/prestadores', AdminPrestadorViewSet, basename='adminprestador')

urlpatterns = router.urls
