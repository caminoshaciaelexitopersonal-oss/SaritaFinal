from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlaceholderViewSet

router = DefaultRouter()
router.register(r'chart-of-accounts', PlaceholderViewSet, basename='chart-of-accounts')
router.register(r'journal-entries', PlaceholderViewSet, basename='journal-entries')
router.register(r'currencies', PlaceholderViewSet, basename='currencies')

urlpatterns = [
    path('', include(router.urls)),
]
