from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from typing import Dict, Any

class CapitanPlanificacionRegional(CapitanTemplate):
    """
    Misión: Orquestar la planificación turística a nivel departamental,
    alineando las estrategias de los municipios y desarrollando planes
    regionales que potencien los atractivos del departamento.
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
            nombre=f"Plan de Planificación Regional",
            descripcion=f"Desarrollar plan regional para el objetivo: {self.objective}"
        )

        # Esta es una aproximación. En una implementación real, podría delegar a varios tenientes.
        self.delegar_tarea(
            plan_tactico=plan_tactico,
            nombre_teniente="planificacion_regional", # Asumiendo que existirá un teniente con esta clave
            descripcion="Ejecutar la planificación turística a nivel departamental.",
            parametros_especificos=self.parametros
        )

        self.lanzar_ejecucion_plan()
        self.logger.info(f"CAPITÁN {self.__class__.__name__}: Planificación completada y tarea delegada a 'planificacion_regional'.")
