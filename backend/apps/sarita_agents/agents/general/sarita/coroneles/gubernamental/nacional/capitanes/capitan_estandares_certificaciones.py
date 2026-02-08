from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from typing import Dict, Any

class CapitanEstandaresCertificaciones(CapitanTemplate):
    """
    Misión: Promover la adopción de estándares de calidad y certificaciones
    turísticas (sostenibilidad, calidad, etc.) entre los prestadores,
    siguiendo los lineamientos y programas nacionales.
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
            nombre=f"Plan de Estándares y Certificaciones",
            descripcion=f"Promover estándares para el objetivo: {mision.directiva_original.get('objective', 'N/A')}"
        )

        self.delegar_tarea(
            plan_tactico=plan_tactico,
            nombre_teniente="estandares_certificaciones",
            descripcion="Promover la adopción de estándares y certificaciones de calidad.",
            parametros_especificos=self.parametros
        )

        # self.lanzar_ejecucion_plan() handled by template
        logger.info(f"CAPITÁN {self.__class__.__name__}: Planificación completada y tarea delegada a 'estandares_certificaciones'.")
