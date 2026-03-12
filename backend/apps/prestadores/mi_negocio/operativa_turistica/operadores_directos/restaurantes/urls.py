from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KitchenStationViewSet, MenuItemDetailViewSet, RestaurantTableViewSet

router = DefaultRouter()
router.register(r'stations', KitchenStationViewSet, basename='restaurant-station')
router.register(r'menu-details', MenuItemDetailViewSet, basename='restaurant-menu-detail')
router.register(r'tables', RestaurantTableViewSet, basename='restaurant-table')

urlpatterns = [
    path('', include(router.urls)),
]
