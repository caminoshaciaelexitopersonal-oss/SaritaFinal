from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from typing import Dict, Any

class CapitanGobernanzaAgentes(CapitanTemplate):
    """
    Misión: Supervisar el comportamiento, rendimiento y ciclo de vida de todos
    los agentes IA (Coroneles, Capitanes, Tenientes), gestionando su
    activación, desactivación, y actualización de políticas operativas.
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
            nombre=f"Plan de Gobernanza de Agentes",
            descripcion=f"Aplicar gobernanza para el objetivo: {mision.directiva_original.get('objective', 'N/A')}"
        )

        self.delegar_tarea(
            plan_tactico=plan_tactico,
            nombre_teniente="gobernanza_agentes",
            descripcion="Ejecutar políticas de gobernanza sobre los agentes.",
            parametros_especificos=self.parametros
        )

        # self.lanzar_ejecucion_plan() handled by template
        logger.info(f"CAPITÁN {self.__class__.__name__}: Planificación completada y tarea delegada a 'gobernanza_agentes'.")
