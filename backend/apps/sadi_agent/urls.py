from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SadiCommandView, AgentExecutionViewSet

app_name = 'sadi_agent'

# El router para el ViewSet de AgentExecution
router = DefaultRouter()
router.register(r'v1/executions', AgentExecutionViewSet, basename='agent-execution')

urlpatterns = [
    # Ruta original para comandos de voz
    path('command/', SadiCommandView.as_view(), name='sadi_command'),

    # Nuevas rutas para la ejecución de agentes bajo /v1/
    path('', include(router.urls)),
]
