from typing import Dict, Any

class CapitanCumplimientoNormativo:
    """
    Misión: Supervisar y asegurar que todas las operaciones del prestador
    cumplan con las normativas turísticas, comerciales y de protección de
    datos vigentes.
    """

    def __init__(self, coronel):
        self.coronel = coronel
        self.context = {}
        print(f"CAPITÁN CUMPLIMIENTO NORMATIVO: Inicializado.")

    def handle_order(self, order: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recibe órdenes para auditar el cumplimiento de una normativa específica.
        """
        print(f"CAPITÁN CUMPLIMIENTO NORMATIVO: Orden recibida - {order['type']}")
        self.context['current_order'] = order

        plan = self.plan()
        delegation_results = self.delegate(plan)
        report = self.report(delegation_results)

        return report

    def plan(self) -> Dict[str, Any]:
        """
        Crea un plan de auditoría de cumplimiento normativo.
        """
        print("CAPITÁN CUMPLIMIENTO NORMATIVO: Creando plan de auditoría normativa...")
        normativa = self.context.get('current_order', {}).get('details', {}).get('normativa')

        planned_steps = {
            "step_1": f"identificar_puntos_de_control_clave_para_{normativa}",
            "step_2": "delegar_revision_de_procesos_y_documentacion",
            "step_3": "evaluar_evidencias_y_detectar_gaps_de_cumplimiento",
            "step_4": "formular_plan_de_remediacion"
        }

        self.context['plan'] = planned_steps
        return planned_steps

    def delegate(self, plan: Dict[str, Any]) -> Dict[str, Any]:
        """
        Delega tareas de revisión a Tenientes auditores de cumplimiento.
        """
        print("CAPITÁN CUMPLIMIENTO NORMATIVO: Delegando auditoría de cumplimiento...")
        results = {}
        for step, task in plan.items():
            print(f"  - Delegando tarea: {task}")
            results[step] = {"status": "DELEGATED", "result": f"Tarea '{task}' delegada para ejecución."}

        self.context['delegation_results'] = results
        return results

    def report(self, delegation_results: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reporta el estado de cumplimiento y las acciones correctivas necesarias.
        """
        print("CAPITÁN CUMPLIMIENTO NORMATIVO: Preparando informe de cumplimiento...")

        report = {
            "captain": self.__class__.__name__,
            "order_id": self.context.get('current_order', {}).get('id', 'N/A'),
            "status": "SUCCESS",
            "result": {
                "message": "Auditoría de cumplimiento normativo completada.",
                "compliance_status": "98% (Se requiere ajuste en política de privacidad)" # Simulado
            }
        }

        print("CAPITÁN CUMPLIMIENTO NORMATIVO: Informe de cumplimiento listo.")
        return report
