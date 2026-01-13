from typing import Dict, Any

class CapitanContextoViaje:
    """
    Misión: Mantener un estado persistente y coherente del viaje actual del
    turista, incluyendo destinos, fechas, reservas hechas y preferencias
    contextuales para personalizar las interacciones.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN CONTEXTO DEL VIAJE: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes para actualizar o recuperar el contexto del viaje.
        """
        print(f"CAPITÁN CONTEXTO DEL VIAJE: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan para gestionar el estado del contexto.
        """
        print("CAPITÁN CONTEXTO DEL VIAJE: Creando plan de gestión de contexto...")
        order_type = self.context.get('current_order', {}).get('type')

        planned_steps = {}
        if order_type == "agregar_reserva_a_contexto":
            planned_steps = {
                "step_1": "validar_datos_de_la_reserva",
                "step_2": "delegar_actualizacion_de_sesion_de_viaje_del_usuario",
                "step_3": "recalcular_sugerencias_basadas_en_nuevo_contexto"
            }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega la persistencia del contexto a un Teniente de gestión de sesiones.
        """
        print("CAPITÁN CONTEXTO DEL VIAJE: Delegando persistencia de contexto...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta el estado actualizado del contexto del viaje.
        """
        print("CAPITÁN CONTEXTO DEL VIAJE: Preparando informe de contexto...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Contexto del viaje actualizado.",
                "current_context_summary": "Viaje a Villavicencio del 15 al 18, hotel reservado." # Simulado
            }
        }

        print("CAPITÁN CONTEXTO DEL VIAJE: Informe de contexto listo.")
        return report
