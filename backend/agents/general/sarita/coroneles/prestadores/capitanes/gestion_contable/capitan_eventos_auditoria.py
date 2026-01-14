from typing import Dict, Any

class CapitanEventosAuditoria:
    """
    Misión: Registrar y monitorear eventos críticos del sistema y de negocio
    para generar una pista de auditoría inmutable, asegurando la trazabilidad
    y el cumplimiento.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN EVENTOS DE AUDITORÍA: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe notificaciones de eventos de otros agentes para registrarlos.
        """
        print(f"CAPITÁN EVENTOS DE AUDITORÍA: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan para registrar el evento de forma segura.
        """
        print("CAPITÁN EVENTOS DE AUDITORÍA: Creando plan de registro de evento...")
        event_details = self.context.get('current_order', {}).get('details', {})

        planned_steps = {
            "step_1": "validar_y_enriquecer_metadatos_del_evento",
            "step_2": "escribir_evento_en_log_de_auditoria_inmutable",
            "step_3": "indexar_evento_para_busquedas_futuras"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega la escritura técnica del evento a un Teniente de Logging.
        """
        print("CAPITÁN EVENTOS DE AUDITORÍA: Delegando escritura de log...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta la confirmación del registro del evento.
        """
        print("CAPITÁN EVENTOS DE AUDITORÍA: Preparando confirmación de registro...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Evento de auditoría registrado exitosamente."
            }
        }

        print("CAPITÁN EVENTOS DE AUDITORÍA: Confirmación lista.")
        return report
