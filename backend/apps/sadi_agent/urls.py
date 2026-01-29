# backend/apps/sadi_agent/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

app_name = 'sadi_agent'

# El router para el ViewSet de AgentExecution
# NOTA: AgentExecutionViewSet no está definido actualmente en views.py
# Se comenta para permitir el arranque del sistema.
router = DefaultRouter()
# router.register(r'v1/executions', AgentExecutionViewSet, basename='agent-execution')

urlpatterns = [
    path('', include(router.urls)),
]
