"""
Módulo de Memoria de Dominio para el Coronel SG-SST.

Este archivo define la estructura de memoria que el Coronel utiliza para
rastrear el estado de las órdenes complejas, desde la planificación hasta
la finalización.
"""

from typing import Dict, Any, List
from enum import Enum
import uuid

class TaskStatus(Enum):
    """Estado de una tarea táctica asignada a un Capitán."""
    PENDING = "PENDIENTE"
    DISPATCHED = "DESPACHADA"
    IN_PROGRESS = "EN_PROGRESO"
    COMPLETED = "COMPLETADA"
    FAILED = "FALLIDA"

class CoronelMemory:
    """
    Gestiona el estado de una orden estratégica completa.

    Esta clase almacena el plan, las tareas descompuestas y el estado de
    cada una de ellas, permitiendo la monitorización y la toma de decisiones.
    """

    def __init__(self, command_id: str):
        """
        Inicializa la memoria para una nueva orden.

        Args:
            command_id (str): Identificador único de la orden recibida del General.
        """
        self.command_id = command_id
        self.strategic_plan: List[str] = []
        self.tasks: Dict[str, Dict[str, Any]] = {}  # task_id -> {details, status, result}
        self.execution_log: List[str] = []
        print(f"MEMORY: Memoria inicializada para la orden '{command_id}'.")

    def store_plan(self, plan: List[str]):
        """Almacena el plan estratégico creado por el Planner."""
        self.strategic_plan = plan
        self.log(f"Plan estratégico almacenado: {plan}")

    def add_task(self, task_details: Dict[str, Any]) -> str:
        """
        Añade una tarea descompuesta a la memoria y le asigna un ID único.

        Args:
            task_details (Dict[str, Any]): Los detalles de la tarea del Decomposer.

        Returns:
            str: El ID único generado para la tarea.
        """
        task_id = str(uuid.uuid4())
        self.tasks[task_id] = {
            "details": task_details,
            "status": TaskStatus.PENDING,
            "result": None,
            "attempts": 0
        }
        self.log(f"Tarea táctica añadida (ID: {task_id}): {task_details}")
        return task_id

    def update_task_status(self, task_id: str, status: TaskStatus, result: Any = None):
        """
        Actualiza el estado y el resultado de una tarea específica.
        """
        if task_id in self.tasks:
            self.tasks[task_id]['status'] = status
            if result:
                self.tasks[task_id]['result'] = result

            if status == TaskStatus.DISPATCHED:
                self.tasks[task_id]['attempts'] += 1

            self.log(f"Estado de la tarea '{task_id}' actualizado a: {status.name}")
        else:
            self.log(f"Error: Intento de actualizar tarea con ID inexistente '{task_id}'.")

    def get_pending_tasks(self) -> List[Dict[str, Any]]:
        """Devuelve todas las tareas que aún no han sido despachadas."""
        return [
            {"id": tid, **tdata} for tid, tdata in self.tasks.items()
            if tdata['status'] == TaskStatus.PENDING
        ]

    def get_full_report(self) -> Dict[str, Any]:
        """Consolida y devuelve un reporte completo del estado de la orden."""
        completed_tasks = sum(1 for t in self.tasks.values() if t['status'] == TaskStatus.COMPLETED)
        total_tasks = len(self.tasks)

        report = {
            "command_id": self.command_id,
            "progress": f"{completed_tasks}/{total_tasks} tareas completadas.",
            "plan": self.strategic_plan,
            "tasks_status": {tid: t['status'].name for tid, t in self.tasks.items()},
            "final_results": {tid: t['result'] for tid, t in self.tasks.items() if t['status'] == TaskStatus.COMPLETED}
        }
        self.log("Generando reporte completo.")
        return report

    def log(self, message: str):
        """Añade un mensaje al log de ejecución."""
        self.execution_log.append(f"[CMD: {self.command_id}] {message}")
