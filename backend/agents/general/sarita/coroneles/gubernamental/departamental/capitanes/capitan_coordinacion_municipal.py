from typing import Dict, Any

class CapitanCoordinacionMunicipal:
    """
    Misión: Actuar como el principal punto de enlace entre el coronel
    departamental y los diferentes entes de turismo municipales, asegurando
    la alineación de estrategias y facilitando la comunicación bidireccional.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN COORDINACIÓN MUNICIPAL: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes para comunicar directrices o recopilar información de los municipios.
        """
        print(f"CAPITÁN COORDINACIÓN MUNICIPAL: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan de comunicación y coordinación con los municipios.
        """
        print("CAPITÁN COORDINACIÓN MUNICIPAL: Creando plan de coordinación...")
        order_details = self.context.get('current_order', {}).get('details', {})

        planned_steps = {
            "step_1": f"identificar_municipios_objetivo_para_{order_details.get('topic')}",
            "step_2": "preparar_paquete_de_comunicacion_o_solicitud_de_datos",
            "step_3": "delegar_contacto_y_seguimiento_a_tenientes_de_enlace",
            "step_4": "consolidar_respuestas_y_feedback_municipal"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega la comunicación directa a Tenientes de enlace asignados a cada municipio.
        """
        print("CAPITÁN COORDINACIÓN MUNICIPAL: Delegando tareas de enlace...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta el resultado de la coordinación al Coronel Departamental.
        """
        print("CAPITÁN COORDINACIÓN MUNICIPAL: Preparando informe de coordinación...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Coordinación con municipios completada.",
                "summary": "Feedback recibido de 5 de 7 municipios contactados." # Simulado
            }
        }

        print("CAPITÁN COORDINACIÓN MUNICIPAL: Informe de coordinación listo.")
        return report
