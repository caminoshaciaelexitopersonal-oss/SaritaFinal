from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, MunicipalityViewSet

router = DefaultRouter()
router.register(r'depts', DepartmentViewSet)
router.register(r'muns', MunicipalityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

