from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from typing import Dict, Any

class CapitanPoliticasNacionales(CapitanTemplate):
    """
    Misión: Monitorear, interpretar y divulgar las políticas, planes y
    regulaciones turísticas emitidas a nivel nacional, asegurando que las
    estrategias regionales y locales estén alineadas con el marco nacional.
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
            nombre=f"Plan de Políticas Nacionales",
            descripcion=f"Analizar políticas para el objetivo: {mision.directiva_original.get('objective', 'N/A')}"
        )

        self.delegar_tarea(
            plan_tactico=plan_tactico,
            nombre_teniente="politicas_nacionales",
            descripcion="Interpretar y divulgar las políticas turísticas nacionales.",
            parametros_especificos=self.parametros
        )

        # self.lanzar_ejecucion_plan() handled by template
        logger.info(f"CAPITÁN {self.__class__.__name__}: Planificación completada y tarea delegada a 'politicas_nacionales'.")
