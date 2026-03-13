from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api.views import GovernmentProfileViewSet, TouristProfileViewSet, DeliveryProfileViewSet, BusinessProfileViewSet

router = DefaultRouter()
router.register(r'government', GovernmentProfileViewSet, basename='government-via')
router.register(r'tourists', TouristProfileViewSet, basename='tourists-via')
router.register(r'delivery', DeliveryProfileViewSet, basename='delivery-via')
router.register(r'business', BusinessProfileViewSet, basename='business-via')

urlpatterns = [
    path('', include(router.urls)),
]
