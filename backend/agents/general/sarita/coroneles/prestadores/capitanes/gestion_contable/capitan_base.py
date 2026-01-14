from typing import Dict, Any

class CapitanContableBase:
    """
    Clase base para los Capitanes de Gestión Contable.
    """

    def __init__(self, coronel, mission: str):
        self.coronel = coronel
        self.mission = mission
        self.context = {}
        print(f"CAPITÁN {self.__class__.__name__}: Inicializado. Misión: {self.mission}")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe y procesa una orden.
        """
        print(f"CAPITÁN {self.__class__.__name__}: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan de acción genérico.
        """
        print(f"CAPITÁN {self.__class__.__name__}: Creando plan de acción...")

        planned_steps = {
            "step_1": "analizar_orden_y_contexto",
            "step_2": "asignar_tenientes_para_ejecucion",
            "step_3": "monitorear_progreso"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega las tareas del plan a los Tenientes.
        """
        print(f"CAPITÁN {self.__class__.__name__}: Delegando tareas a Tenientes...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta el resultado de la operación.
        """
        print(f"CAPITÁN {self.__class__.__name__}: Preparando informe de resultados...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": f"Misión '{self.mission}' completada exitosamente."
            }
        }

        print(f"CAPITÁN {self.__class__.__name__}: Informe listo.")
        return report
