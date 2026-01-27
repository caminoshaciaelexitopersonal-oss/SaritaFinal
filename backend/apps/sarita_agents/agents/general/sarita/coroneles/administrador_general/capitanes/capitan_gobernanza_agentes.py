from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from typing import Dict, Any

class CapitanGobernanzaAgentes(CapitanTemplate):
    """
    Misión: Supervisar el comportamiento, rendimiento y ciclo de vida de todos
    los agentes IA (Coroneles, Capitanes, Tenientes), gestionando su
    activación, desactivación, y actualización de políticas operativas.
    """

    def __init__(self, mision_id: str, objective: str, parametros: Dict[str, Any]):
        super().__init__(mision_id=mision_id, objective=objective, parametros=parametros)
        self.logger.info(f"CAPITÁN {self.__class__.__name__}: Inicializado para Misión ID {self.mision_id}.")

    def plan(self):
        """
        El corazón del Capitán. Aquí es donde defines el plan táctico.
        """
        self.logger.info(f"CAPITÁN {self.__class__.__name__}: Planificando la misión.")

        plan_tactico = self.get_or_create_plan_tactico(
            nombre=f"Plan de Gobernanza de Agentes",
            descripcion=f"Aplicar gobernanza para el objetivo: {self.objective}"
        )

        self.delegar_tarea(
            plan_tactico=plan_tactico,
            nombre_teniente="gobernanza_agentes",
            descripcion="Ejecutar políticas de gobernanza sobre los agentes.",
            parametros_especificos=self.parametros
        )

        self.lanzar_ejecucion_plan()
        self.logger.info(f"CAPITÁN {self.__class__.__name__}: Planificación completada y tarea delegada a 'gobernanza_agentes'.")
