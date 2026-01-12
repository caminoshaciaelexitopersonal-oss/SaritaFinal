from typing import Dict, Any

class CapitanReservasTurista:
    """
    Misión: Gestionar el proceso de reserva de un servicio turístico, desde la
    selección hasta la confirmación y el pago.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN RESERVAS DEL TURISTA: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe una orden para crear o gestionar una reserva.
        """
        print(f"CAPITÁN RESERVAS DEL TURISTA: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan para el flujo de reserva.
        """
        print("CAPITÁN RESERVAS DEL TURISTA: Creando plan de reserva...")
        service_id = self.context.get('current_order', {}).get('details', {}).get('service_id')

        planned_steps = {
            "step_1": f"verificar_disponibilidad_de_{service_id}",
            "step_2": "bloquear_temporalmente_el_servicio",
            "step_3": "delegar_procesamiento_de_pago_a_teniente_financiero",
            "step_4": "confirmar_reserva_y_enviar_voucher"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega tareas críticas como el procesamiento de pagos a Tenientes especializados.
        """
        print("CAPITÁN RESERVAS DEL TURISTA: Delegando tareas de reserva...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta el estado de la reserva al Capitán de Experiencia.
        """
        print("CAPITÁN RESERVAS DEL TURISTA: Preparando informe de reserva...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Reserva confirmada exitosamente.",
                "reservation_id": "RES-12345XYZ" # Simulado
            }
        }

        print("CAPITÁN RESERVAS DEL TURISTA: Informe de reserva listo.")
        return report
