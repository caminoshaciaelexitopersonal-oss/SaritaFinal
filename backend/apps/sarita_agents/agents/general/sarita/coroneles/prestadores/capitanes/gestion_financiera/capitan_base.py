from apps.sarita_agents.agents.capitan_template import CapitanTemplate
from typing import Dict, Any

class CapitanFinancieraBase(CapitanTemplate):
    """
    Clase base para los capitanes del módulo de Gestión Financiera.
    Hereda de CapitanBase para mantener la jerarquía y especialización del coronel.
    """

    def __init__(self, coronel):
        super().__init__(coronel=coronel)
        logger.info(f"CAPITÁN CapitanFinancieraBase: Inicializado para Misión ID {mision.id}.")

    def plan(self, mision):
        """
        El corazón del Capitán. Aquí es donde defines el plan táctico.
        Debes crear un PlanTáctico y luego delegar Tareas a los Tenientes.
        """
        logger.info(f"CAPITÁN CapitanFinancieraBase: Planificando la misión.")

        # 1. Crear el Plan Táctico
        plan_tactico = self.coronel.get_or_create_plan_tactico(
            nombre="Plan de Ejecución para CapitanFinancieraBase",
            descripcion=f"Este plan detalla los pasos para cumplir el objetivo: {mision.directiva_original.get('objective', 'N/A')}"
        )

        # 2. Definir y Delegar Tareas (EJEMPLO - DEBE SER IMPLEMENTADO)
        # self.delegar_tarea(plan_tactico=plan_tactico, nombre_teniente="...", descripcion="...", parametros_especificos={...})

        # 3. Lanzar la Ejecución del Plan
        # self.lanzar_ejecucion_plan() handled by template

        logger.info(f"CAPITÁN CapitanFinancieraBase: Planificación completada y tareas delegadas.")
