"""
Módulo Principal del Coronel de Dominio SG-SST.

Este archivo contiene la clase `CoronelSST`, que actúa como el comandante
estratégico para el dominio de Seguridad y Salud en el Trabajo. Orquesta
a los demás componentes para ejecutar órdenes complejas recibidas del
General Sarita.
"""

from typing import Dict, Any
# Importa las clases de los otros módulos del Coronel
from .policies import SSTPolicies
from .memory import CoronelMemory, TaskStatus
from .planner import SSTPlanner
from .task_decomposer import SSTTaskDecomposer
from .captain_router import SSTCaptainRouter

class CoronelSST:
    """
    Orquesta la ejecución de órdenes de SG-SST.
    """

    def __init__(self):
        """
        Inicializa el Coronel y todos sus componentes internos.
        """
        self.policies = SSTPolicies()
        self.planner = SSTPlanner(self.policies)
        self.decomposer = SSTTaskDecomposer(self.policies)
        self.router = SSTCaptainRouter()
        self.active_memory: Dict[str, CoronelMemory] = {}
        print("CORONEL SST: Inicializado y listo para recibir comandos.")

    def receive_command(self, command: Dict[str, Any]) -> Dict[str, Any]:
        """
        Punto de entrada para los comandos del General Sarita.
        """
        command_id = command.get("id", "cmd_sin_id")
        objective = command.get("objective", {})

        print(f"\n--- CORONEL SST: Nuevo Comando Recibido (ID: {command_id}) ---")
        print(f"Objetivo: {objective}")

        # 1. Crear memoria para esta orden
        self.active_memory[command_id] = CoronelMemory(command_id)

        # 2. Analizar y Planificar
        plan = self.plan_execution(command_id, objective)
        if not plan:
            return self.report_to_general(command_id, {"status": "FAILED", "message": "No se pudo generar un plan."})

        # 3. Descomponer y Despachar (simulado en un solo paso por ahora)
        self.dispatch_to_captains(command_id, plan, command.get("context", {}))

        # 4. Monitorear y Consolidar (simulación)
        final_report = self.consolidate_results(command_id)

        # 5. Reportar al General
        return self.report_to_general(command_id, final_report)

    def plan_execution(self, command_id: str, objective: Dict[str, Any]) -> list:
        """
        Utiliza el Planner para crear un plan estratégico.
        """
        memory = self.active_memory[command_id]
        memory.log("Iniciando fase de planificación.")

        plan = self.planner.create_plan(objective)

        if plan:
            memory.store_plan(plan)
        else:
            memory.log("Fallo en la planificación: El objetivo no generó un plan.")

        return plan

    def dispatch_to_captains(self, command_id: str, plan: list, context: Dict[str, Any]):
        """
        Itera sobre el plan, descompone cada fase y enruta las tareas.
        """
        memory = self.active_memory[command_id]
        memory.log(f"Iniciando despacho para {len(plan)} fases del plan.")

        for phase in plan:
            memory.log(f"Procesando fase: '{phase}'")

            # Descomponer la fase en tareas
            tasks = self.decomposer.decompose_phase(phase, context)

            for task_details in tasks:
                # Añadir a la memoria y obtener ID
                task_id = memory.add_task(task_details)

                # Enrutar para obtener asignación
                assignment = self.router.route_task(task_details)

                # Despachar (simulación)
                print(f"  -> Despachando tarea '{task_id}' al Capitán '{assignment['target_captain_id']}'...")
                memory.update_task_status(task_id, TaskStatus.DISPATCHED)

    def consolidate_results(self, command_id: str) -> Dict[str, Any]:
        """
        Simula la espera y consolidación de resultados de los capitanes.
        """
        memory = self.active_memory[command_id]
        memory.log("Iniciando consolidación de resultados.")

        # Simulación: Marcamos algunas tareas como completadas y otras como fallidas
        all_tasks = memory.tasks.keys()
        for i, task_id in enumerate(all_tasks):
            if i % 4 != 0: # Falla 1 de cada 4 tareas
                memory.update_task_status(task_id, TaskStatus.COMPLETED, {"detail": "Ejecución exitosa."})
            else:
                memory.update_task_status(task_id, TaskStatus.FAILED, {"error": "Conexión con equipo fallida."})

        return memory.get_full_report()

    def report_to_general(self, command_id: str, result: Dict[str, Any]) -> Dict[str, Any]:
        """
        Formatea el resultado final para enviarlo de vuelta al General.
        """
        print(f"--- CORONEL SST: Reporte Final para Comando (ID: {command_id}) ---")
        print(result)

        # Limpiar memoria después de completar la orden
        if command_id in self.active_memory:
            del self.active_memory[command_id]
            print(f"Memoria para el comando '{command_id}' liberada.")

        return result

# Ejemplo de uso
if __name__ == '__main__':
    coronel_sst = CoronelSST()

    orden_del_general = {
        "id": "auditoria-hotel-xyz-001",
        "objective": {
            "action": "realizar_auditoria_mensual",
            "target_type": "instalacion"
        },
        "context": {
            "target_id": "hotel_xyz"
        }
    }

    coronel_sst.receive_command(orden_del_general)
