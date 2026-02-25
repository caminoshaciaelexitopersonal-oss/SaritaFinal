from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EnterprisePolicyViewSet, StrategicObjectiveViewSet,
    CorporateBudgetViewSet, EnterpriseWorkflowViewSet,
    DecisionLogViewSet, ScenarioSimulationViewSet,
    RollingForecastViewSet, RiskExposureViewSet, DecisionRuleViewSet
)

router = DefaultRouter()
router.register(r'policies', EnterprisePolicyViewSet, basename='enterprise-policy')
router.register(r'objectives', StrategicObjectiveViewSet, basename='strategic-objective')
router.register(r'budgets', CorporateBudgetViewSet, basename='corporate-budget')
router.register(r'workflows', EnterpriseWorkflowViewSet, basename='enterprise-workflow')
router.register(r'decisions', DecisionLogViewSet, basename='decision-log')
router.register(r'simulations', ScenarioSimulationViewSet, basename='strategic-simulation')
router.register(r'forecasts', RollingForecastViewSet, basename='rolling-forecast')
router.register(r'risks', RiskExposureViewSet, basename='risk-exposure')
router.register(r'rules', DecisionRuleViewSet, basename='decision-rule')

urlpatterns = [
    path('', include(router.urls)),
]
