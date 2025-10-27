from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlaceholderViewSet

router = DefaultRouter()
router.register(r'bank-accounts', PlaceholderViewSet, basename='bank-accounts')
router.register(r'cash-transactions', PlaceholderViewSet, basename='cash-transactions')

urlpatterns = [
    path('', include(router.urls)),
]
