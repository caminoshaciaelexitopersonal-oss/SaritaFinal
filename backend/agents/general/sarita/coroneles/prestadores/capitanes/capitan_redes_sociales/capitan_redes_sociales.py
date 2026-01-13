from typing import Dict, Any

class CapitanRedesSociales:
    """
    Misión: Gestionar la interacción de la marca en redes sociales de forma
    automatizada, desde la detección de mensajes hasta la respuesta o el
    escalamiento a un agente humano.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN REDES SOCIALES: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe notificaciones de nuevos eventos de redes sociales.
        """
        print(f"CAPITÁN REDES SOCIALES: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan de procesamiento para cada interacción.
        """
        print("CAPITÁN REDES SOCIALES: Creando plan de procesamiento de mensaje...")

        planned_steps = {
            "step_1": {"teniente": "monitoreo_mensajes", "task": "capturar_nuevo_evento"},
            "step_2": {"teniente": "clasificacion_intencion", "task": "analizar_texto_mensaje"},
            "step_3": {"teniente": "respuesta_automatica", "task": "enviar_respuesta_via_api"},
            # El escalamiento sería condicional
            # "step_4": {"teniente": "escalamiento_humano", "task": "crear_ticket_en_sistema_de_soporte"}
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega cada paso del procesamiento del mensaje a sus tenientes.
        """
        print("CAPITÁN REDES SOCIALES: Delegando procesamiento de mensaje...")
        results = {}
        for step, details in plan.items():
            print(f"  - Delegando tarea '{details['task']}' a Teniente '{details['teniente']}'")
            results[step] = {"status": "DELEGATED", "result": "Tarea simulada completada por teniente."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta la gestión de la interacción al Coronel.
        """
        print("CAPITÁN REDES SOCIALES: Preparando informe de interacción...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "summary": "Interacción en redes sociales gestionada automáticamente."
        }

        print("CAPITÁN REDES SOCIALES: Informe listo.")
        return report
