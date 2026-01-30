from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OptimizationProposalViewSet

router = DefaultRouter()
router.register(r'proposals', OptimizationProposalViewSet)

app_name = 'ecosystem_optimization'

urlpatterns = [
    path('', include(router.urls)),
]
