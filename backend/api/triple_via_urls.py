from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GovernmentProfileViewSet, TouristProfileViewSet, DeliveryProfileViewSet,
    BusinessProfileViewSet, BusinessStaffViewSet, UserViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users-via-compat')
router.register(r'government', GovernmentProfileViewSet, basename='government-via')
router.register(r'tourists', TouristProfileViewSet, basename='tourists-via')
router.register(r'delivery', DeliveryProfileViewSet, basename='delivery-via')
router.register(r'business', BusinessProfileViewSet, basename='business-via')
router.register(r'business-staff', BusinessStaffViewSet, basename='business-staff-via')
router.register(r'turismo/providers', TourismProviderViewSet, basename='turismo-provider-v1')
router.register(r'turismo/services', TourismServiceViewSet, basename='turismo-service-v1')

urlpatterns = [
    path('', include(router.urls)),
]
