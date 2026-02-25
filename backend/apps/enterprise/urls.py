from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EnterprisePolicyViewSet, StrategicObjectiveViewSet,
    CorporateBudgetViewSet, EnterpriseWorkflowViewSet,
    DecisionLogViewSet
)

router = DefaultRouter()
router.register(r'policies', EnterprisePolicyViewSet, basename='enterprise-policy')
router.register(r'objectives', StrategicObjectiveViewSet, basename='strategic-objective')
router.register(r'budgets', CorporateBudgetViewSet, basename='corporate-budget')
router.register(r'workflows', EnterpriseWorkflowViewSet, basename='enterprise-workflow')
router.register(r'decisions', DecisionLogViewSet, basename='decision-log')

urlpatterns = [
    path('', include(router.urls)),
]
