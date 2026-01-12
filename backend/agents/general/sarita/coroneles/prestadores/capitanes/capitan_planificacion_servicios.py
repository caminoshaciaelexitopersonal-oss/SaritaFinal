from typing import Dict, Any

class CapitanPlanificacionServicios:
    """
    Misión: Diseñar y estructurar nuevos servicios turísticos o modificar los existentes.
    Se encarga de definir recursos, costos, itinerarios y capacidades.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN PLANIFICACIÓN DE SERVICIOS: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe una orden del Coronel para planificar un servicio.
        """
        print(f"CAPITÁN PLANIFICACIÓN DE SERVICIOS: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan detallado para la estructuración del servicio.
        """
        print("CAPITÁN PLANIFICACIÓN DE SERVICIOS: Creando plan de estructuración...")
        service_details = self.context.get('current_order', {}).get('details', {})

        planned_steps = {
            "step_1": f"definir_itinerario_para_{service_details.get('nombre', 'nuevo_servicio')}",
            "step_2": "calcular_costos_operativos",
            "step_3": "asignar_requerimientos_de_recursos",
            "step_4": "establecer_precio_de_venta"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega tareas específicas a Tenientes (e.g., Teniente de Finanzas para costos).
        """
        print("CAPITÁN PLANIFICACIÓN DE SERVICIOS: Delegando tareas a Tenientes...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            # Simulación de delegación
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta el plan de servicio finalizado al Coronel o al Capitán General.
        """
        print("CAPITÁN PLANIFICACIÓN DE SERVICIOS: Preparando informe de planificación...")

        final_status = "SUCCESS"

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": final_status,
            "result": {
                "message": "Plan de servicio estructurado exitosamente.",
                "plan_details": self.context.get('plan')
            }
        }

        print("CAPITÁN PLANIFICACIÓN DE SERVICIOS: Informe final listo.")
        return report
