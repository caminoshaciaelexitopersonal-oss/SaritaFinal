from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from typing import Dict, Any

class CapitanMonitoreoPlataforma(CapitanTemplate):
    """
    Misión: Vigilar la salud y el rendimiento general de la plataforma,
    monitorizando métricas clave (CPU, memoria, latencia de red, errores),
    y generando alertas proactivas ante posibles incidentes.
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
            nombre=f"Plan de Monitoreo de Plataforma",
            descripcion=f"Ejecutar monitoreo para el objetivo: {self.objective}"
        )

        self.delegar_tarea(
            plan_tactico=plan_tactico,
            nombre_teniente="monitoreo_plataforma",
            descripcion="Realizar el chequeo de salud y rendimiento de la plataforma.",
            parametros_especificos=self.parametros
        )

        self.lanzar_ejecucion_plan()
        self.logger.info(f"CAPITÁN {self.__class__.__name__}: Planificación completada y tarea delegada a 'monitoreo_plataforma'.")
