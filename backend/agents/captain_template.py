from typing import Dict, Any

class CapitanTemplate:
    """
    Misión: [Descripción clara y concisa de la responsabilidad del Capitán]
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN [Nombre del Capitán]: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe una orden del Coronel, la procesa y gestiona su ejecución.
        """
        print(f"CAPITÁN [Nombre del Capitán]: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan táctico para cumplir la orden recibida.
        No ejecuta, solo planifica.
        """
        print("CAPITÁN [Nombre del Capitán]: Creando plan táctico...")
        planned_steps = {
            "step_1": "placeholder_task_1",
            "step_2": "placeholder_task_2",
        }
        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega la ejecución de los pasos del plan a los Tenientes (aún no creados).
        Simula la delegación por ahora.
        """
        print("CAPITÁN [Nombre del Capitán]: Delegando tareas a Tenientes...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada exitosamente."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta el estado y resultado de la operación al Coronel.
        """
        print("CAPITÁN [Nombre del Capitán]: Preparando informe para el Coronel...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "details": delegation_results
        }

        print("CAPITÁN [Nombre del Capitán]: Informe final listo.")
        return report
