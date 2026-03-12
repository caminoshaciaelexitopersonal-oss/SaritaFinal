from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .provider_views import (
    TourismProviderViewSet, BusinessProfileViewSet,
    TourismServiceViewSet, ReservationViewSet
)

router = DefaultRouter()
router.register(r'tourism-providers', TourismProviderViewSet, basename='tourism-provider')
router.register(r'business-profiles', BusinessProfileViewSet, basename='business-profile')
router.register(r'tourism-services', TourismServiceViewSet, basename='tourism-service')
router.register(r'tourism-reservations', ReservationViewSet, basename='tourism-reservation')

urlpatterns = [
    path('', include(router.urls)),
]
