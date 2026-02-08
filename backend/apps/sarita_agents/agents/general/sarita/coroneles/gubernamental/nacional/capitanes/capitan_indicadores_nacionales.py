from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from typing import Dict, Any

class CapitanIndicadoresNacionales(CapitanTemplate):
    """
    Misión: Recopilar, analizar y reportar los indicadores clave de turismo
    a nivel nacional (ocupación, gasto promedio, etc.), comparando el
    desempeño del departamento con las métricas nacionales.
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
            nombre=f"Plan de Indicadores Nacionales",
            descripcion=f"Analizar indicadores para el objetivo: {mision.directiva_original.get('objective', 'N/A')}"
        )

        self.delegar_tarea(
            plan_tactico=plan_tactico,
            nombre_teniente="indicadores_nacionales",
            descripcion="Recopilar y analizar los indicadores de turismo nacionales.",
            parametros_especificos=self.parametros
        )

        # self.lanzar_ejecucion_plan() handled by template
        logger.info(f"CAPITÁN {self.__class__.__name__}: Planificación completada y tarea delegada a 'indicadores_nacionales'.")
