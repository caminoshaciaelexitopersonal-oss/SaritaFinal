from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, MunicipalityViewSet
from .provider_views import (
    TourismProviderViewSet, BusinessProfileViewSet,
    TourismServiceViewSet, ReservationViewSet,
    TourismSubClassificationViewSet
)
from .route_views import TourismRouteViewSet

router = DefaultRouter()
router.register(r'depts', DepartmentViewSet)
router.register(r'muns', MunicipalityViewSet)
router.register(r'tourism-providers', TourismProviderViewSet)
router.register(r'tourism-services', TourismServiceViewSet)
router.register(r'tourism-reservations', ReservationViewSet)
router.register(r'intelligent-routes', TourismRouteViewSet)
router.register(r'sub-classifications', TourismSubClassificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

