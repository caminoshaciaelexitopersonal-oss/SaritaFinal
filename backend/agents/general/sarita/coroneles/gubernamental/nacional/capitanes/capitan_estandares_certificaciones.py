from typing import Dict, Any

class CapitanEstandaresCertificaciones:
    """
    Misión: Gestionar el ciclo de vida de los estándares de calidad y las
    certificaciones turísticas a nivel nacional, desde su definición hasta
    el proceso de otorgamiento y renovación.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN ESTÁNDARES Y CERTIFICACIONES: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes para crear un nuevo estándar o gestionar una solicitud de certificación.
        """
        print(f"CAPITÁN ESTÁNDARES Y CERTIFICACIONES: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan para la gestión del estándar o la certificación.
        """
        print("CAPITÁN ESTÁNDARES Y CERTIFICACIONES: Creando plan de gestión...")
        order_type = self.context.get('current_order', {}).get('type')

        planned_steps = {}
        if order_type == "evaluar_solicitud_certificacion":
            details = self.context.get('current_order', {}).get('details', {})
            prestador_id = details.get('prestador_id')
            cert_type = details.get('cert_type')

            planned_steps = {
                "step_1": f"verificar_documentacion_de_solicitud_para_{prestador_id}",
                "step_2": f"delegar_auditoria_en_sitio_segun_estandares_de_{cert_type}",
                "step_3": "evaluar_informe_de_auditoria_y_tomar_decision",
                "step_4": "notificar_resultado_al_prestador"
            }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega la auditoría en sitio a Tenientes auditores calificados.
        """
        print("CAPITÁN ESTÁNDARES Y CERTIFICACIONES: Delegando tareas de auditoría...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta el resultado del proceso de certificación al Coronel Nacional.
        """
        print("CAPITÁN ESTÁNDARES Y CERTIFICACIONES: Preparando informe de certificación...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Proceso de certificación finalizado.",
                "decision": "APROBADO" # Simulado
            }
        }

        print("CAPITÁN ESTÁNDARES Y CERTIFICACIONES: Informe de certificación listo.")
        return report
