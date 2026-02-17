from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AmenityViewSet, RoomTypeViewSet, RoomViewSet

router = DefaultRouter()
router.register(r'amenities', AmenityViewSet, basename='hotel-amenity')
router.register(r'room-types', RoomTypeViewSet, basename='hotel-room-type')
router.register(r'rooms', RoomViewSet, basename='hotel-room')

urlpatterns = [
    path('', include(router.urls)),
]
