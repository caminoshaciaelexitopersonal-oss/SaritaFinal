
# Las URLs de SADI han sido migradas a la arquitectura de Sarita Agents.
# Este archivo se mantiene por ahora, pero su contenido será redefinido
# o eliminado en futuras fases.

from django.urls import path


app_name = 'sadi_agent'

# El router para el ViewSet de AgentExecution
router = DefaultRouter()
router.register(r'v1/executions', AgentExecutionViewSet, basename='agent-execution')

urlpatterns = [

    # Las rutas se definirán aquí en el futuro si es necesario.

]
