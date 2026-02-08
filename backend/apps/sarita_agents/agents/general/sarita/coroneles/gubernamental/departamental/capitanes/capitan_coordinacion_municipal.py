from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from typing import Dict, Any

class CapitanCoordinacionMunicipal(CapitanTemplate):
    """
    Misión: Servir como enlace entre el nivel departamental y los municipios,
    facilitando la comunicación, recogiendo datos, y asegurando que las
    políticas y planes regionales se implementen de forma coordinada.
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
            nombre=f"Plan de Coordinación Municipal",
            descripcion=f"Coordinar con municipios para el objetivo: {mision.directiva_original.get('objective', 'N/A')}"
        )

        self.delegar_tarea(
            plan_tactico=plan_tactico,
            nombre_teniente="coordinacion_municipal",
            descripcion="Ejecutar la coordinación con los diferentes municipios.",
            parametros_especificos=self.parametros
        )

        # self.lanzar_ejecucion_plan() handled by template
        logger.info(f"CAPITÁN {self.__class__.__name__}: Planificación completada y tarea delegada a 'coordinacion_municipal'.")
