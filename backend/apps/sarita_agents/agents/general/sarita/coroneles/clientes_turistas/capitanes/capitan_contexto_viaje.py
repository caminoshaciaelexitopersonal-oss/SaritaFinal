from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from typing import Dict, Any

class CapitanContextoViaje(CapitanTemplate):
    """
    Misión: Mantener y comprender el contexto completo del viaje de un turista,
    incluyendo fechas, destinos, compañeros de viaje, y preferencias,
    para anticipar necesidades y ofrecer asistencia proactiva.
    """

    def __init__(self, coronel):
        super().__init__(coronel=coronel)
        logger.info(f"CAPITÁN {self.__class__.__name__}: Inicializado para Misión ID {mision.id}.")

    def plan(self, mision):
        """
        El corazón del Capitán. Aquí es donde defines el plan táctico.
        """
        logger.info(f"CAPITÁN {self.__class__.__name__}: Planificando la misión.")

        plan_tactico = self.coronel.get_or_create_plan_tactico(
            nombre=f"Plan de Contexto de Viaje",
            descripcion=f"Gestionar contexto para el objetivo: {mision.directiva_original.get('objective', 'N/A')}"
        )

        self.delegar_tarea(
            plan_tactico=plan_tactico,
            nombre_teniente="contexto_viaje",
            descripcion="Analizar y actualizar el contexto del viaje del turista.",
            parametros_especificos=self.parametros
        )

        # self.lanzar_ejecucion_plan() handled by template
        logger.info(f"CAPITÁN {self.__class__.__name__}: Planificación completada y tarea delegada a 'contexto_viaje'.")
