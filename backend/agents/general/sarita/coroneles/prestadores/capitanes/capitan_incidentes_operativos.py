from typing import Dict, Any

class CapitanIncidentesOperativos:
    """
    Misión: Gestionar y resolver cualquier imprevisto o incidente que ocurra
    durante la prestación de un servicio, minimizando el impacto en el cliente.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN INCIDENTES OPERATIVOS: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe una alerta de incidente y activa el protocolo de respuesta.
        """
        print(f"CAPITÁN INCIDENTES OPERATIVOS: Alerta de incidente recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan de acción inmediato para contener y resolver el incidente.
        """
        print("CAPITÁN INCIDENTES OPERATIVOS: Creando plan de resolución...")
        incident_type = self.context.get('current_order', {}).get('details', {}).get('incident_type')

        planned_steps = {
            "step_1": f"clasificar_severidad_del_incidente_{incident_type}",
            "step_2": "activar_protocolo_de_respuesta_adecuado",
            "step_3": "notificar_a_los_afectados_y_al_mando",
            "step_4": "asignar_teniente_de_resolucion"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega tareas específicas del plan de resolución a Tenientes de campo o soporte.
        """
        print("CAPITÁN INCIDENTES OPERATIVOS: Delegando tareas de resolución...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            # Simulación de delegación
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución inmediata."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta el estado del incidente y las acciones tomadas al Capitán General.
        """
        print("CAPITÁN INCIDENTES OPERATIVOS: Preparando informe de incidente...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "ACTION_TAKEN",
            "result": {
                "message": "Protocolo de resolución de incidentes activado.",
                "incident_status": "CONTENIDO"
            }
        }

        print("CAPITÁN INCIDENTES OPERATIVOS: Informe de incidente listo.")
        return report
