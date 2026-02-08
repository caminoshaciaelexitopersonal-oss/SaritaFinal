from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from typing import Dict, Any

class CapitanControlPrestadores(CapitanTemplate):
    """
    Misión: Supervisar y controlar a los prestadores de servicios turísticos
    del municipio, asegurando el cumplimiento de la normativa, la calidad
    del servicio y la formalización (RNT).
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
            nombre=f"Plan de Control de Prestadores",
            descripcion=f"Supervisar prestadores para el objetivo: {mision.directiva_original.get('objective', 'N/A')}"
        )

        self.delegar_tarea(
            plan_tactico=plan_tactico,
            nombre_teniente="control_prestadores",
            descripcion="Ejecutar la supervisión y control de los prestadores de servicios.",
            parametros_especificos=self.parametros
        )

        # self.lanzar_ejecucion_plan() handled by template
        logger.info(f"CAPITÁN {self.__class__.__name__}: Planificación completada y tarea delegada a 'control_prestadores'.")
