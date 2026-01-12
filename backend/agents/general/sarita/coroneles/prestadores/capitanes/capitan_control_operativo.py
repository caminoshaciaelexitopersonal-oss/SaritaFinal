from typing import Dict, Any

class CapitanControlOperativo:
    """
    Misión: Supervisar la ejecución en tiempo real de los servicios turísticos,
    asegurando que se cumplan los itinerarios y estándares de calidad planificados.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN CONTROL OPERATIVO: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe una orden para monitorear un servicio en ejecución.
        """
        print(f"CAPITÁN CONTROL OPERATIVO: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan de monitoreo para el servicio.
        """
        print("CAPITÁN CONTROL OPERATIVO: Creando plan de monitoreo...")
        service_id = self.context.get('current_order', {}).get('details', {}).get('service_id')

        planned_steps = {
            "step_1": f"establecer_puntos_de_control_para_{service_id}",
            "step_2": "asignar_teniente_de_campo_para_seguimiento",
            "step_3": "definir_protocolo_de_comunicacion_de_estado"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega la ejecución del monitoreo a Tenientes en campo.
        """
        print("CAPITÁN CONTROL OPERATIVO: Delegando monitoreo a Tenientes...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            # Simulación de delegación
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta el estado del servicio en tiempo real al Capitán General o al Coronel.
        """
        print("CAPITÁN CONTROL OPERATIVO: Preparando informe de estado...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "IN_PROGRESS",
            "result": {
                "message": "Monitoreo del servicio activo.",
                "current_status": "Todos los puntos de control OK."
            }
        }

        print("CAPITÁN CONTROL OPERATIVO: Informe de estado listo.")
        return report
