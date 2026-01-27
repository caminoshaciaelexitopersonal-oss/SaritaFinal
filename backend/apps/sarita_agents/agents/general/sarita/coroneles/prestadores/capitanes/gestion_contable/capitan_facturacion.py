from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from typing import Dict, Any

class CapitanFacturacion(CapitanTemplate):
    """
    Misión: Gestionar la emisión, envío y seguimiento de facturas de venta, asegurando la correcta facturación de todos los servicios prestados.
    """

    def __init__(self, mision_id: str, objective: str, parametros: Dict[str, Any]):
        super().__init__(mision_id=mision_id, objective=objective, parametros=parametros)
        self.logger.info(f"CAPITÁN CapitanFacturacion: Inicializado para Misión ID {self.mision_id}.")

    def plan(self):
        """
        El corazón del Capitán. Aquí es donde defines el plan táctico.
        Debes crear un PlanTáctico y luego delegar Tareas a los Tenientes.
        """
        self.logger.info(f"CAPITÁN CapitanFacturacion: Planificando la misión.")

        # 1. Crear el Plan Táctico
        plan_tactico = self.get_or_create_plan_tactico(
            nombre="Plan de Ejecución para CapitanFacturacion",
            descripcion=f"Este plan detalla los pasos para cumplir el objetivo: {self.objective}"
        )

        # 2. Definir y Delegar Tareas (EJEMPLO - DEBE SER IMPLEMENTADO)
        # self.delegar_tarea(plan_tactico=plan_tactico, nombre_teniente="...", descripcion="...", parametros_especificos={...})

        # 3. Lanzar la Ejecución del Plan
        self.lanzar_ejecucion_plan()

        self.logger.info(f"CAPITÁN CapitanFacturacion: Planificación completada y tareas delegadas.")
