from typing import Dict, Any

class CapitanPQRS:
    """
    Misión: Gestionar el ciclo de vida de las Peticiones, Quejas, Reclamos y
    Sugerencias (PQRS) de los turistas, asegurando su registro, enrutamiento
    y seguimiento hasta la resolución.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN PQRS: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe una nueva solicitud de PQRS.
        """
        print(f"CAPITÁN PQRS: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan para el procesamiento de la PQRS.
        """
        print("CAPITÁN PQRS: Creando plan de gestión de PQRS...")
        pqrs_type = self.context.get('current_order', {}).get('details', {}).get('type')

        planned_steps = {
            "step_1": f"generar_numero_de_caso_unico_para_{pqrs_type}",
            "step_2": "categorizar_y_priorizar_la_solicitud",
            "step_3": "delegar_asignacion_a_teniente_de_soporte_adecuado",
            "step_4": "enviar_confirmacion_de_recepcion_al_usuario"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega la gestión del caso a los Tenientes de soporte.
        """
        print("CAPITÁN PQRS: Delegando caso a Tenientes de Soporte...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta que la PQRS ha sido registrada y está en proceso.
        """
        print("CAPITÁN PQRS: Preparando informe de registro de caso...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Solicitud PQRS registrada y en proceso.",
                "case_id": "PQRS-98765" # Simulado
            }
        }

        print("CAPITÁN PQRS: Informe de caso listo.")
        return report
