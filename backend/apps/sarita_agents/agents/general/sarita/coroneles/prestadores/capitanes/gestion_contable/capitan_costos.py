from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from typing import Dict, Any

class CapitanCostos(CapitanTemplate):
    """
    Misión: Analizar y controlar los costos operativos y de servicios, proporcionando información clave para la toma de decisiones y la optimización de recursos.
    """

    def __init__(self, mision_id: str, objective: str, parametros: Dict[str, Any]):
        super().__init__(mision_id=mision_id, objective=objective, parametros=parametros)
        self.logger.info(f"CAPITÁN CapitanCostos: Inicializado para Misión ID {self.mision_id}.")

    def plan(self):
        """
        El corazón del Capitán. Aquí es donde defines el plan táctico.
        Debes crear un PlanTáctico y luego delegar Tareas a los Tenientes.
        """
        self.logger.info(f"CAPITÁN CapitanCostos: Planificando la misión.")

        # 1. Crear el Plan Táctico
        plan_tactico = self.get_or_create_plan_tactico(
            nombre="Plan de Ejecución para CapitanCostos",
            descripcion=f"Este plan detalla los pasos para cumplir el objetivo: {self.objective}"
        )

        # 2. Definir y Delegar Tareas (EJEMPLO - DEBE SER IMPLEMENTADO)
        # self.delegar_tarea(plan_tactico=plan_tactico, nombre_teniente="...", descripcion="...", parametros_especificos={...})

        # 3. Lanzar la Ejecución del Plan
        self.lanzar_ejecucion_plan()

        self.logger.info(f"CAPITÁN CapitanCostos: Planificación completada y tareas delegadas.")
